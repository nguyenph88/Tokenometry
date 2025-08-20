# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2025-08-19

### Changed
- **Major dependency updates for modern Python compatibility**
- Updated pandas from `>=1.5.0` to `>=2.1.0` for latest features and performance
- Updated numpy from `>=1.21.0,<2.0.0` to `>=1.24.0,<2.0.0` for pandas-ta compatibility
- Updated matplotlib from `>=3.5.0` to `>=3.7.0` for enhanced plotting capabilities
- Updated coinbase-advanced-py to `>=0.5.0` for latest API features
- Updated development tools: pytest `>=7.4.0`, black `>=23.0.0`, flake8 `>=6.0.0`, mypy `>=1.5.0`

### Fixed
- **Resolved numpy compatibility issues** with pandas-ta library
- Fixed pandas FutureWarning deprecation issues
- Enhanced error handling for missing data and indicator columns
- Improved data validation and robustness in core analysis functions
- Added proper warnings suppression for cleaner output

### Technical
- **Modernized package structure** with pyproject.toml as primary configuration
- Removed legacy setup.py to eliminate configuration conflicts
- Enhanced pandas operations with error handling and data validation
- Improved ATR column reference handling for better reliability
- Added comprehensive data existence checks throughout the analysis pipeline

### Compatibility
- **Python 3.8+** support maintained
- **pandas 2.1.0+** compatibility with modern DataFrame operations
- **numpy 1.24.0-1.26.4** range for optimal pandas-ta integration
- **Cross-platform** compatibility verified on Windows, macOS, and Linux
- **Modern Python packaging** standards with setuptools 68.0.0+

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
