# Tokenometry

[![PyPI version](https://badge.fury.io/py/tokenometry.svg)](https://badge.fury.io/py/tokenometry)
[![Python versions](https://img.shields.io/pypi/pyversions/tokenometry.svg)](https://pypi.org/project/tokenometry/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sophisticated, multi-strategy crypto analysis bot for generating trading signals based on technical analysis, market sentiment, and on-chain data.

## 🚀 Features

- **Multi-Strategy Support**: Day trading, swing trading, and long-term investment strategies
- **Multi-Timeframe Analysis**: Combines higher timeframe trends with lower timeframe signals
- **Technical Indicators**: EMA/SMA crossovers, RSI, MACD, ATR for comprehensive analysis
- **Risk Management**: Automatic stop-loss calculation and position sizing
- **Professional Logging**: Comprehensive audit trail and monitoring
- **API Integration**: Coinbase Advanced Trade API for real-time data
- **Configurable**: Easy strategy customization through configuration dictionaries

## 📦 Installation

```bash
pip install tokenometry
```

## 🎯 Quick Start

```python
from tokenometry import Tokenometry
import logging

# Configure your strategy
config = {
    "STRATEGY_NAME": "Day Trader",
    "PRODUCT_IDS": ["BTC-USD", "ETH-USD"],
    "GRANULARITY_SIGNAL": "FIVE_MINUTE",
    "GRANULARITY_TREND": "ONE_HOUR",
    "SHORT_PERIOD": 9,
    "LONG_PERIOD": 21,
    "RISK_PER_TRADE_PERCENTAGE": 0.5,
    "ATR_STOP_LOSS_MULTIPLIER": 2.0,
    # ... more configuration options
}

# Initialize the bot
logger = logging.getLogger("MyBot")
bot = Tokenometry(config=config, logger=logger)

# Run analysis
signals = bot.scan()
for signal in signals:
    print(f"Signal: {signal}")
```

## 🎲 Strategy Configurations

### Day Trader (High-Frequency)
- **Timeframe**: 5-minute signals, 1-hour trend
- **Best for**: Active day traders, scalping
- **Risk**: 0.5% per trade

### Swing Trader (Medium-Term)
- **Timeframe**: 4-hour signals, daily trend
- **Best for**: Part-time traders, swing trading
- **Risk**: 1.0% per trade

### Long-Term Investor
- **Timeframe**: Daily signals, weekly trend
- **Best for**: Position traders, long-term investors
- **Risk**: 1.0% per trade

## 🔧 Configuration Options

```python
config = {
    "STRATEGY_NAME": "Custom Strategy",
    "PRODUCT_IDS": ["BTC-USD", "ETH-USD", "SOL-USD"],
    "GRANULARITY_SIGNAL": "FIVE_MINUTE",  # Signal timeframe
    "GRANULARITY_TREND": "ONE_HOUR",      # Trend timeframe
    "SHORT_PERIOD": 9,                    # Fast EMA/SMA period
    "LONG_PERIOD": 21,                    # Slow EMA/SMA period
    "RSI_PERIOD": 14,                     # RSI calculation period
    "RSI_OVERBOUGHT": 70,                 # RSI overbought threshold
    "RSI_OVERSOLD": 30,                   # RSI oversold threshold
    "MACD_FAST": 12,                      # MACD fast period
    "MACD_SLOW": 26,                      # MACD slow period
    "MACD_SIGNAL": 9,                     # MACD signal period
    "ATR_PERIOD": 14,                     # ATR calculation period
    "HYPOTHETICAL_PORTFOLIO_SIZE": 100000.0,  # Portfolio size for calculations
    "RISK_PER_TRADE_PERCENTAGE": 1.0,    # Risk per trade percentage
    "ATR_STOP_LOSS_MULTIPLIER": 2.5,     # ATR multiplier for stop-loss
}
```

## 📊 Signal Types

- **BUY**: Golden cross + bullish trend + RSI not overbought + MACD bullish
- **SELL**: Death cross + bearish trend + RSI not oversold + MACD bearish
- **HOLD**: No crossover or trend misalignment

## 🛡️ Risk Management

- **Automatic Stop-Loss**: Calculated using ATR for volatility-adjusted stops
- **Position Sizing**: Based on your risk percentage and stop-loss distance
- **Portfolio Protection**: Each trade risks only the specified percentage

## 📝 Logging & Monitoring

```python
import logging

# Set up logging
logger = logging.getLogger("MyBot")
logger.setLevel(logging.INFO)

# Console output
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# File logging
file_handler = logging.FileHandler("trading_bot.log")
logger.addHandler(file_handler)
```

## 🔌 API Requirements

- **Coinbase Advanced Trade API**: Required for price data
- **NewsAPI** (optional): For sentiment analysis
- **Glassnode API** (optional): For on-chain data

## 📚 Examples

Check out the `examples/` directory for complete working examples:

- `example_usage.py`: Basic usage with all three strategies
- Custom strategy configurations
- Risk management examples

## 🧪 Testing

```bash
# Install development dependencies
pip install tokenometry[dev]

# Run tests
pytest tests/
```

## 📈 Performance

- **Analysis Speed**: Optimized for real-time trading
- **Memory Usage**: Efficient data handling with pandas
- **API Efficiency**: Smart pagination and rate limiting
- **Scalability**: Configurable for multiple assets and timeframes

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for analytical and educational purposes only. It is **not financial advice**. The signals generated are based on algorithmic analysis and do not guarantee any specific outcome. Always conduct your own research and consult with a qualified financial advisor before making investment decisions.

## 🔗 Links

- **Documentation**: [GitHub README](https://github.com/nguyenph88/Tokenometry#readme)
- **Source Code**: [GitHub Repository](https://github.com/nguyenph88/Tokenometry)
- **Issues**: [GitHub Issues](https://github.com/nguyenph88/Tokenometry/issues)
- **Changelog**: [CHANGELOG.md](https://github.com/nguyenph88/Tokenometry/blob/main/CHANGELOG.md)

---

**Made with ❤️ for the crypto trading community**
