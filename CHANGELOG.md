# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.6] - 2025-08-19

### Added
- **Volume Filter Enhancement** for improved signal quality
- **Volume Moving Average calculation** to identify significant volume spikes
- **Volume spike multiplier configuration** for customizable sensitivity
- **Enhanced signal filtering** that requires volume confirmation for technical crossovers

### Features
- **Volume Filter Parameters**:
  - `VOLUME_FILTER_ENABLED`: Enable/disable volume filtering (default: False)
  - `VOLUME_MA_PERIOD`: Period for volume moving average calculation (default: 20)
  - `VOLUME_SPIKE_MULTIPLIER`: Multiplier for volume spike detection (default: 2.0)
- **Improved Signal Quality**: Only generates signals when volume confirms technical crossovers
- **Configurable Sensitivity**: Different volume multipliers for different trading strategies

### Technical
- **Enhanced SMA calculation** to support volume column calculations
- **Volume confirmation logic** integrated into signal generation pipeline
- **Backward compatibility** maintained - volume filter is optional and disabled by default

### Strategy Configurations
- **Day Trader**: Volume spike multiplier 2.0 (high sensitivity for quick moves)
- **Swing Trader**: Volume spike multiplier 1.5 (moderate sensitivity)
- **Long-Term**: Volume spike multiplier 1.5 (moderate sensitivity)

## [1.0.5] - 2025-08-19

### Fixed
- **Resolved critical import conflict** that caused `'LOOKBACK_DAYS'` errors when running from subdirectories
- **Fixed package installation conflicts** between development and installed versions
- **Eliminated cached bytecode issues** that persisted across code changes
- **Resolved module import path conflicts** when running examples from different directories

### Changed
- **Improved package installation process** with proper development mode setup
- **Enhanced example file structure** for better reliability and consistency
- **Cleaned up conflicting example files** that contained outdated code references

### Technical
- **Resolved Python module import precedence** issues between local and installed packages
- **Fixed site-packages vs local development** version conflicts
- **Improved package distribution** with proper editable install support
- **Enhanced development workflow** with consistent import behavior across all directories

### Compatibility
- **Consistent behavior** across all execution contexts (root directory, subdirectories, examples)
- **Reliable package imports** regardless of execution location
- **Proper development environment** setup for contributors and users

## [1.0.4] - 2025-08-19

### Changed
- **Removed pandas-ta dependency** to resolve Python 3.13 compatibility issues
- **Replaced external technical indicators** with custom implementations using standard pandas and numpy
- **Enhanced Python 3.13 support** by eliminating problematic third-party dependencies

### Added
- **Custom technical indicator calculations**:
  - Simple Moving Average (SMA) using pandas rolling window
  - Exponential Moving Average (EMA) using pandas ewm
  - Relative Strength Index (RSI) with proper gain/loss calculations
  - MACD (Moving Average Convergence Divergence) with signal line
  - Average True Range (ATR) for volatility measurement
- **Improved error handling** for missing data and indicator columns
- **Enhanced logging** for better debugging and monitoring

### Fixed
- **Python 3.13 compatibility** issues resolved by removing pandas-ta
- **Dependency conflicts** eliminated with modern Python environments
- **Technical indicator reliability** improved with custom implementations
- **Data validation** enhanced throughout the analysis pipeline

### Technical
- **Self-contained indicator calculations** using only pandas and numpy
- **Optimized performance** with vectorized operations
- **Better memory management** without external library overhead
- **Improved maintainability** with custom, well-documented functions

### Compatibility
- **Python 3.8+** support maintained and enhanced
- **pandas 2.1.0+** compatibility verified
- **numpy 1.24.0+** compatibility improved
- **Cross-platform** compatibility maintained
- **Modern Python packaging** standards preserved

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
