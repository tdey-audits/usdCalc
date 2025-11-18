# INR ⇄ USD Currency Converter

A standalone desktop application for converting between Indian Rupees (INR) and US Dollars (USD) with both command-line (CLI) and graphical (GUI) interfaces.

## Features

- **Bidirectional Conversion**: Convert from USD to INR and vice versa
- **Live Exchange Rates**: Automatically fetches current exchange rates from API
- **CLI & GUI Modes**: Use from terminal or launch graphical interface
- **Modern UI**: Black, white, and red color scheme with Inter and Instrument Serif fonts
- **Simple & Intuitive**: Just type in either field to see instant conversion
- **Offline Support**: Uses cached rates when offline
- **Cross-platform**: Works on macOS and Linux

## Installation

### Homebrew (macOS and Linux)

The easiest way to install is via Homebrew:

```bash
brew install inr-usd-converter
```

For Linux users, you may need to install Homebrew (Linuxbrew) first:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Manual Installation

If you prefer not to use Homebrew:

1. Clone or download this repository
2. Make sure Python 3.8+ is installed
3. For GUI mode, ensure Tkinter is available:
   ```bash
   # Ubuntu/Debian
   sudo apt install python3-tk
   
   # Fedora
   sudo dnf install python3-tkinter
   
   # Arch Linux
   sudo pacman -S tk
   ```
4. Run the application:
   ```bash
   python3 currency_converter.py
   ```

## Usage

### Command Line Interface (CLI)

After installation via Homebrew, use the `inr-usd-converter` command:

```bash
# Convert 100 USD to INR
inr-usd-converter 100 usd

# Convert 1000 INR to USD
inr-usd-converter 1000 inr

# Display current exchange rate
inr-usd-converter --rate

# Use higher precision (e.g., 4 decimal places)
inr-usd-converter 50.50 usd --precision 4

# Use cached rate without fetching live data
inr-usd-converter 100 usd --no-fetch

# Show help
inr-usd-converter --help

# Show version
inr-usd-converter --version
```

**Example Output:**

```
$ inr-usd-converter 100 usd
$100.00 USD = ₹8,312.00 INR
(Live rate: 1 USD = ₹83.12 INR)

$ inr-usd-converter 5000 inr
₹5,000.00 INR = $60.14 USD
(Live rate: 1 USD = ₹83.12 INR)

$ inr-usd-converter --rate
1 USD = ₹83.12 INR (live rate)
```

### Graphical User Interface (GUI)

Launch the GUI application:

```bash
# Via the dedicated GUI command
inr-usd-converter-gui

# Or by running without arguments
inr-usd-converter
```

On Linux with Homebrew, you can also find "INR-USD Converter" in your application menu.

**Using the GUI:**

1. Enter an amount in either the USD or INR field
2. See instant conversion in the other field
3. Click "Refresh Rate" to update to the latest exchange rate
4. The current exchange rate is displayed at the bottom

### Python Module

You can also use the converter as a Python module:

```python
from currency_converter import CurrencyConverter

converter = CurrencyConverter()
usd_amount = 100
inr_amount = converter.usd_to_inr(usd_amount)
print(f"${usd_amount} = ₹{inr_amount:.2f}")
```

## Requirements

- **Python**: 3.8 or higher
- **Tkinter**: Required for GUI mode (usually pre-installed with Python)
- **Standard Library**: Uses only Python standard library (json, urllib, datetime, etc.)
- **Internet**: Optional - fetches live rates when available, falls back to cached/default rates

## Design

- **Color Scheme**: Black (#000000), White (#FFFFFF), and Red (#FF0000)
- **Typography**: 
  - Inter font for UI elements and body text
  - Instrument Serif font for headings and accents
  - Graceful fallback to system fonts if custom fonts unavailable
- **Layout**: Clean, minimal interface with clear visual hierarchy

## How It Works

- Fetches live exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/)
- Rates are cached for 1 hour to minimize API calls
- If the API is unavailable, uses a sensible default rate (₹83.12 per USD)
- Conversions happen instantly as you type (GUI mode)
- CLI mode supports flexible options for offline use and precision control

## Development

### Running Tests

```bash
python3 test_converter.py
```

### File Structure

```
.
├── currency_converter.py    # Main application (CLI + GUI)
├── test_converter.py        # Test suite
├── pyproject.toml           # Python package configuration
├── setup.py                 # Setup script for installation
├── Formula/
│   └── inr-usd-converter.rb # Homebrew formula
├── resources/
│   └── inr-usd-converter.desktop # Linux desktop entry
├── README.md                # This file
├── USAGE.md                 # Detailed usage guide
├── FEATURES.md              # Design and features
├── LICENSE                  # MIT License
└── requirements.txt         # Python dependencies (none)
```

## Troubleshooting

### CLI Issues

**Command not found:**
```bash
# Make sure Homebrew's bin is in your PATH
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
# Or on macOS:
export PATH="/usr/local/bin:$PATH"
```

### GUI Issues

**"ModuleNotFoundError: No module named 'tkinter'":**

Install the tkinter package:
```bash
sudo apt install python3-tk        # Ubuntu/Debian
sudo dnf install python3-tkinter   # Fedora
sudo pacman -S tk                  # Arch Linux
brew reinstall python@3.11         # macOS (Homebrew)
```

**Fonts not displaying correctly:**

The application will work with system default fonts if Inter and Instrument Serif are not available. For the best experience, install these fonts from [Google Fonts](https://fonts.google.com/).

**Cannot fetch exchange rates:**

If you're offline or the API is unavailable, the app will use a cached or default exchange rate. Use the `--no-fetch` flag to skip API calls entirely.

## Platform Notes

### macOS

- Tkinter is included with Homebrew's Python
- GUI launches without additional dependencies
- Can be run from Terminal or application launcher

### Linux

- May require separate `python3-tk` package installation
- Desktop entry is installed to `~/.local/share/applications/` (manual install) or `/home/linuxbrew/.linuxbrew/share/applications/` (Homebrew)
- Works on all major distributions (Ubuntu, Fedora, Arch, etc.)

## Contributing

This is an open-source project. Contributions, issues, and feature requests are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## API Credits

Exchange rates provided by [ExchangeRate-API](https://www.exchangerate-api.com/)
