# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2025-08-19

### Added
- Initial PyPI package release
- Multi-strategy trading bot framework
- Support for Day Trading, Swing Trading, and Long-Term Investment strategies
- Technical analysis indicators: EMA, RSI, MACD, ATR
- Multi-timeframe analysis (MTA) capabilities
- Automated risk management with position sizing
- Comprehensive logging and monitoring
- Coinbase Advanced Trade API integration

### Features
- **Day Trader Strategy**: 5-minute signals with 1-hour trend confirmation
- **Swing Trader Strategy**: 4-hour signals with daily trend confirmation  
- **Long-Term Strategy**: Daily signals with weekly trend confirmation
- Configurable risk parameters and portfolio management
- Professional logging system with dual output (console and file)

### Technical
- Modular architecture with clean separation of concerns
- Configurable strategy parameters via dictionary configuration
- Efficient data fetching with pagination support
- Error handling and graceful degradation
- Cross-platform compatibility (Windows, macOS, Linux)

## [1.0.1] - 2025-08-19

### Changed
- Refactored from milestone-based scripts to modular library
- Renamed class from CryptoScanner to Tokenometry
- Improved code organization and maintainability

### Fixed
- Resolved pandas FutureWarning issues
- Fixed Coinbase API response handling
- Corrected batch fetching logic for historical data
- Updated pandas warning paths for compatibility

## [1.0.0] - 2025-08-19

### Added
- Initial milestone-based implementation
- Basic SMA crossover strategy
- RSI and MACD confluence filters
- ATR-based risk management
- Multi-asset scanning capabilities
