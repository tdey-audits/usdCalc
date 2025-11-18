# Release Notes - INR-USD Converter v1.0.0

## What's New

This is the initial release of the INR-USD Currency Converter with full CLI and GUI support, packaged for Homebrew/Linuxbrew distribution.

## Key Features

### Dual Interface
- **Command-Line Interface (CLI)**: Fast conversions from terminal
- **Graphical User Interface (GUI)**: Interactive desktop application

### Installation Methods
- **Homebrew/Linuxbrew**: One-command installation on macOS and Linux
- **Python pip**: Install as a Python package
- **Manual**: Direct execution from source

### Core Functionality
- Bidirectional INR ⇄ USD currency conversion
- Live exchange rates from exchangerate-api.com
- Offline support with cached/default rates
- High-contrast black/white/red design
- Inter and Instrument Serif typography

## Installation

### Via Homebrew (Recommended)

```bash
# Add tap (if not already added)
brew tap tdey-audits/tools

# Install
brew install inr-usd-converter
```

### Via pip

```bash
# From source
git clone https://github.com/tdey-audits/usdCalc.git
cd usdCalc
pip install .
```

### Manual

```bash
# Clone and run
git clone https://github.com/tdey-audits/usdCalc.git
cd usdCalc
chmod +x currency_converter.py
./currency_converter.py --help
```

## Usage Examples

### CLI Mode

```bash
# Convert currencies
inr-usd-converter 100 usd
inr-usd-converter 5000 inr

# Check exchange rate
inr-usd-converter --rate

# Use offline mode
inr-usd-converter 100 usd --no-fetch

# Custom precision
inr-usd-converter 50.5 usd --precision 4

# Show help
inr-usd-converter --help
```

### GUI Mode

```bash
# Launch GUI
inr-usd-converter-gui

# Or run without arguments
inr-usd-converter
```

## What's Included

### Executables
- `inr-usd-converter` - Main CLI/GUI launcher
- `inr-usd-converter-gui` - Direct GUI launcher

### Documentation
- `README.md` - Main documentation
- `CLI.md` - CLI usage guide
- `USAGE.md` - GUI usage guide
- `HOMEBREW.md` - Homebrew installation guide
- `FEATURES.md` - Feature overview
- `QUICKSTART.md` - Quick start guide

### Files
- `currency_converter.py` - Main application
- `test_converter.py` - Test suite
- `Formula/inr-usd-converter.rb` - Homebrew formula
- `resources/` - Desktop integration files

## System Requirements

### CLI Mode
- Python 3.8+
- Standard library only (no external dependencies)
- Works without Tkinter

### GUI Mode
- Python 3.8+
- Tkinter (usually pre-installed)
- Optional: Inter and Instrument Serif fonts

## Platform Support

- ✅ macOS (via Homebrew)
- ✅ Linux (via Linuxbrew)
  - Ubuntu/Debian
  - Fedora
  - Arch Linux
  - Other distributions

## Homebrew Integration

### macOS
- Automatic PATH integration
- Full Tkinter support via Homebrew Python
- Clean installation and updates

### Linux
- Linuxbrew installation
- Desktop menu integration (`.desktop` file)
- Automatic dependency handling

## Known Limitations

1. **Tkinter Requirement**: GUI mode requires Tkinter. On some Linux systems, install separately:
   ```bash
   sudo apt install python3-tk  # Debian/Ubuntu
   ```

2. **Font Availability**: Custom fonts (Inter, Instrument Serif) are optional. The app works with system fonts.

3. **API Dependency**: Exchange rates require internet. Offline mode uses cached/default rates.

4. **Currency Pair**: Only INR-USD conversion supported in this version.

## Troubleshooting

### Command Not Found (Linux)

```bash
# Add Homebrew to PATH
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```

### GUI Won't Launch

```bash
# Check Tkinter
python3 -c "import tkinter"

# Install if needed
sudo apt install python3-tk  # Debian/Ubuntu
brew reinstall python@3.11   # macOS
```

### Rate Fetch Failures

```bash
# Use offline mode
inr-usd-converter 100 usd --no-fetch
```

## Upgrading

```bash
# Update Homebrew
brew update

# Upgrade the package
brew upgrade inr-usd-converter
```

## Uninstalling

```bash
brew uninstall inr-usd-converter
```

On Linux, this also removes the desktop entry.

## Testing

Run the test suite:

```bash
python3 test_converter.py
```

All tests should pass. The test suite includes:
- Currency conversion logic tests
- API fetch tests (if online)
- CLI interface tests
- Edge case handling

## Contributing

This is an open-source project. Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT License - See [LICENSE](LICENSE) for details.

## Credits

- **Exchange Rate Data**: [ExchangeRate-API](https://www.exchangerate-api.com/)
- **Fonts**: Inter by Rasmus Andersson, Instrument Serif by Google Fonts
- **Platform**: Python 3 + Tkinter
- **Distribution**: Homebrew/Linuxbrew

## Links

- **Repository**: https://github.com/tdey-audits/usdCalc
- **Issues**: https://github.com/tdey-audits/usdCalc/issues
- **Homebrew Formula**: Formula/inr-usd-converter.rb

## What's Next

Future versions may include:
- Additional currency pairs
- Historical rate tracking
- Rate change notifications
- Conversion history
- Theme customization

## Support

For help:
1. Check the documentation (README.md, CLI.md, USAGE.md)
2. Run `inr-usd-converter --help` for CLI help
3. Report issues on GitHub

---

**Version**: 1.0.0  
**Release Date**: 2024  
**Maintainer**: INR-USD Converter Team
