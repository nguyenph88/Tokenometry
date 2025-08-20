#!/usr/bin/env python3

import sys
import os

print("=== DEBUG TEST ===")
print(f"Python path: {sys.path}")
print(f"Current directory: {os.getcwd()}")

try:
    import tokenometry
    print(f"Tokenometry imported from: {tokenometry.__file__}")
    
    from tokenometry import Tokenometry
    print(f"Tokenometry class module: {Tokenometry.__module__}")
    
    # Test the actual method that's failing
    from examples.example_usage import create_day_trader_config
    config = create_day_trader_config()
    print(f"Config keys: {list(config.keys())}")
    
    # Test direct call
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('debug')
    
    scanner = Tokenometry(config, logger)
    print("Testing direct _get_historical_data call...")
    result = scanner._get_historical_data('BTC-USD', 'ONE_HOUR')
    print(f"Direct call result: {result is not None}")
    
    print("Testing scan method...")
    signals = scanner.scan()
    print(f"Scan completed, signals: {len(signals)}")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
