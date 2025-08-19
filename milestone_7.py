# milestone_7.py

import time
import pandas as pd
import pandas_ta as ta
from coinbase.rest import RESTClient
import warnings
import logging
import sys

# --- Setup Logging ---
def setup_logger():
    """Configures a logger to output to both console and a file."""
    # Create a logger object
    logger = logging.getLogger('CryptoBot')
    logger.setLevel(logging.INFO) # Set the minimum level of messages to log

    # Prevent the logger from propagating messages to the root logger
    logger.propagate = False

    # Remove any existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler('bot_activity.log', mode='a') # 'a' for append
    file_handler.setLevel(logging.INFO)

    # Create a console handler to print logs to the console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()

# Suppress SettingWithCopyWarning
warnings.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)

# --- Configuration ---
PRODUCT_IDS = ["BTC-USD", "ETH-USD", "SOL-USD", "AVAX-USD"] 
GRANULARITY_SIGNAL = "ONE_DAY"
GRANULARITY_TREND = "ONE_WEEK"
TREND_SMA_PERIOD = 30
SHORT_WINDOW, LONG_WINDOW = 50, 200
RSI_PERIOD = 14
RSI_OVERBOUGHT, RSI_OVERSOLD = 70, 30
MACD_FAST, MACD_SLOW, MACD_SIGNAL = 12, 26, 9
ATR_PERIOD = 14

# --- Risk Management ---
HYPOTHETICAL_PORTFOLIO_SIZE = 100000.0
RISK_PER_TRADE_PERCENTAGE = 1.0
ATR_STOP_LOSS_MULTIPLIER = 2.5

def get_historical_data(product_id, granularity, years=1):
    """Fetches historical candlestick data from Coinbase."""
    logger.info(f"Fetching {granularity} data for {product_id}...")
    try:
        client = RESTClient()
        end_time = int(time.time())
        start_time = end_time - (years * 365 * 86400)
        
        # Determine seconds per candle for pagination
        granularity_seconds = {"ONE_DAY": 86400, "ONE_WEEK": 604800}.get(granularity, 86400)
        
        logger.info(f"  Time range: {pd.to_datetime(start_time, unit='s').date()} to {pd.to_datetime(end_time, unit='s').date()}")
        logger.info(f"  Estimated total periods: {(end_time - start_time) / granularity_seconds:.0f}")
        logger.info(f"  Estimated API calls needed: {((end_time - start_time) / granularity_seconds / 300):.1f}")
        
        all_candles = []
        current_start = start_time
        batch_count = 0

        while current_start < end_time:
            batch_count += 1
            current_end = current_start + (300 * granularity_seconds)
            if current_end > end_time: current_end = end_time

            logger.info(f"  Batch {batch_count}: Fetching from {pd.to_datetime(current_start, unit='s').date()} to {pd.to_datetime(current_end, unit='s').date()}...")
            response = client.get_public_candles(product_id=product_id, start=str(current_start), end=str(current_end), granularity=granularity)
            
            # Convert response to dictionary and extract candles
            response_dict = response.to_dict()
            candles = response_dict.get('candles', [])
            if not candles: break
            all_candles.extend(candles)
            # Move to the next batch by advancing 300 periods (not 1 period)
            current_start = current_end
            time.sleep(0.5)

        if not all_candles: return None
        df = pd.DataFrame(all_candles)
        df.rename(columns={'start': 'timestamp', 'low': 'Low', 'high': 'High', 'open': 'Open', 'close': 'Close', 'volume': 'Volume'}, inplace=True)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        for col in ['Low', 'High', 'Open', 'Close', 'Volume']: df[col] = pd.to_numeric(df[col])
        df.drop_duplicates(subset='timestamp', inplace=True)
        df.set_index('timestamp', inplace=True)
        df.sort_index(inplace=True)
        return df
    except Exception as e:
        logger.error(f"An error occurred fetching data for {product_id}: {e}")
        return None

def get_long_term_trend(product_id):
    """Determines the long-term market trend using a weekly SMA."""
    df_weekly = get_historical_data(product_id, GRANULARITY_TREND, years=3)
    if df_weekly is None or df_weekly.empty: return "Unknown"
    df_weekly.ta.sma(length=TREND_SMA_PERIOD, append=True)
    df_weekly.dropna(inplace=True)
    latest_week = df_weekly.iloc[-1]
    trend_sma_col = f'SMA_{TREND_SMA_PERIOD}'
    return "Bullish" if latest_week['Close'] > latest_week[trend_sma_col] else "Bearish"

def calculate_indicators(df):
    """Calculates all necessary technical indicators."""
    if df is None: return None
    df.ta.sma(length=SHORT_WINDOW, append=True)
    df.ta.sma(length=LONG_WINDOW, append=True)
    df.ta.rsi(length=RSI_PERIOD, append=True)
    df.ta.macd(fast=MACD_FAST, slow=MACD_SLOW, signal=MACD_SIGNAL, append=True)
    df.ta.atr(length=ATR_PERIOD, append=True)
    return df

def generate_signals(df):
    """Generates buy/sell/hold signals based on the 3-factor confluence strategy."""
    if df is None: return None
    # Column names
    short_sma, long_sma = f'SMA_{SHORT_WINDOW}', f'SMA_{LONG_WINDOW}'
    rsi_col = f'RSI_{RSI_PERIOD}'
    macd_line, macd_signal = f'MACD_{MACD_FAST}_{MACD_SLOW}_{MACD_SIGNAL}', f'MACDs_{MACD_FAST}_{MACD_SLOW}_{MACD_SIGNAL}'
    
    df['Signal'] = 0
    # Buy conditions
    golden_cross = (df[short_sma] > df[long_sma]) & (df[short_sma].shift(1) <= df[long_sma].shift(1))
    rsi_buy = df[rsi_col] < RSI_OVERBOUGHT
    macd_buy = df[macd_line] > df[macd_signal]
    df.loc[golden_cross & rsi_buy & macd_buy, 'Signal'] = 1

    # Sell conditions
    death_cross = (df[short_sma] < df[long_sma]) & (df[short_sma].shift(1) >= df[long_sma].shift(1))
    rsi_sell = df[rsi_col] > RSI_OVERSOLD
    macd_sell = df[macd_line] < df[macd_signal]
    df.loc[death_cross & rsi_sell & macd_sell, 'Signal'] = -1
    return df

def main():
    """Main function to run the multi-asset analysis with MTA filter and logging."""
    logger.info("--- Starting Crypto Analysis Bot Run ---")
    
    for product_id in PRODUCT_IDS:
        logger.info(f"--- Analyzing {product_id} ---")
        long_term_trend = get_long_term_trend(product_id)
        logger.info(f"Long-term trend for {product_id}: {long_term_trend}")

        data = get_historical_data(product_id, GRANULARITY_SIGNAL, years=1)
        if data is not None and not data.empty:
            data = calculate_indicators(data)
            data.dropna(inplace=True)
            data = generate_signals(data)
            
            latest = data.iloc[-1]
            signal, price = latest['Signal'], latest['Close']
            
            # --- APPLY MTA FILTER ---
            final_signal = "HOLD"
            if signal == 1 and long_term_trend == "Bullish": final_signal = "BUY"
            elif signal == -1 and long_term_trend == "Bearish": final_signal = "SELL"
            
            logger.info(f"Signal for {product_id}: {final_signal} at ${price:,.2f}")

            if final_signal == "BUY":
                atr = latest[f'ATRr_{ATR_PERIOD}']
                stop_loss = price - (atr * ATR_STOP_LOSS_MULTIPLIER)
                capital_to_risk = HYPOTHETICAL_PORTFOLIO_SIZE * (RISK_PER_TRADE_PERCENTAGE / 100)
                stop_dist = price - stop_loss
                if stop_dist > 0:
                    pos_size_crypto = capital_to_risk / stop_dist
                    pos_size_usd = pos_size_crypto * price
                    log_msg = (f"TRADE PLAN FOR {product_id}: Entry=${price:,.2f}, "
                               f"Stop=${stop_loss:,.2f}, "
                               f"Size={pos_size_crypto:.6f} ({product_id.split('-')[0]}) or ${pos_size_usd:,.2f}")
                    logger.info(log_msg)
        else:
            logger.warning(f"Could not process daily data for {product_id}, skipping.")
            
    logger.info("--- Crypto Analysis Bot Run Finished ---")

if __name__ == "__main__":
    main()
