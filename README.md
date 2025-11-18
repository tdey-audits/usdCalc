# INR ⇄ USD Currency Converter

A standalone desktop application for converting between Indian Rupees (INR) and US Dollars (USD) with a clean, modern interface.

## Features

- **Bidirectional Conversion**: Convert from USD to INR and vice versa
- **Live Exchange Rates**: Automatically fetches current exchange rates from API
- **Modern UI**: Black, white, and red color scheme with Inter and Instrument Serif fonts
- **Simple & Intuitive**: Just type in either field to see instant conversion
- **Offline Support**: Uses cached rates when offline

## Requirements

- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

## Installation & Setup

### 1. Install Python

Most Linux distributions come with Python 3 pre-installed. Check your version:

```bash
python3 --version
```

If Python is not installed, install it using your package manager:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-tk
```

**Fedora:**
```bash
sudo dnf install python3 python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S python tk
```

### 2. Install Fonts (Optional but Recommended)

For the best visual experience, install the Inter and Instrument Serif fonts:

**Inter Font:**
```bash
# Download and install Inter font
wget https://github.com/rsms/inter/releases/download/v3.19/Inter-3.19.zip
unzip Inter-3.19.zip -d Inter
sudo mkdir -p /usr/share/fonts/truetype/inter
sudo cp Inter/Inter\ Desktop/*.ttf /usr/share/fonts/truetype/inter/
sudo fc-cache -f -v
```

**Instrument Serif Font:**
```bash
# Download from Google Fonts or use system serif font as fallback
# The app will work with system default fonts if these are not available
```

Alternatively, you can use the system's font manager to install these fonts from Google Fonts.

## Running the Application

### Method 1: Direct Execution

Make the script executable and run it:

```bash
chmod +x currency_converter.py
./currency_converter.py
```

### Method 2: Using Python

```bash
python3 currency_converter.py
```

### Method 3: Create Desktop Launcher (Optional)

Create a desktop entry for easy access:

```bash
# Create .desktop file
cat > ~/.local/share/applications/currency-converter.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=INR-USD Converter
Comment=Currency converter between INR and USD
Exec=/usr/bin/python3 $(pwd)/currency_converter.py
Icon=accessories-calculator
Terminal=false
Categories=Utility;Finance;
EOF

# Update desktop database
update-desktop-database ~/.local/share/applications/
```

Now you can launch the app from your application menu.

## Usage

1. **Launch the application** using any of the methods above
2. **Enter an amount** in either the USD or INR field
3. **See instant conversion** in the other field
4. **Refresh rate** using the "Refresh Rate" button to get the latest exchange rate
5. The current exchange rate is displayed at the bottom of the converter

## How It Works

- The app fetches live exchange rates from a free API (exchangerate-api.com)
- Rates are cached for 1 hour to minimize API calls
- If the API is unavailable, it uses a sensible default rate (₹83.12 per USD)
- Conversions happen instantly as you type

## Troubleshooting

### "ModuleNotFoundError: No module named 'tkinter'"

Install the tkinter package:
```bash
sudo apt install python3-tk  # Ubuntu/Debian
sudo dnf install python3-tkinter  # Fedora
```

### Fonts not displaying correctly

The application will work with system default fonts if Inter and Instrument Serif are not available. For the best experience, install the fonts as described in the setup section.

### Cannot fetch exchange rates

If you're offline or the API is unavailable, the app will use a cached or default exchange rate. You'll see a message indicating whether you're using a live or default rate.

## Design

- **Color Scheme**: Black (#000000), White (#FFFFFF), and Red (#FF0000)
- **Typography**: 
  - Inter font for UI elements and body text
  - Instrument Serif font for headings and accents
- **Layout**: Clean, minimal interface with clear visual hierarchy

## License

This project is open source and available for personal and commercial use.

## API Credits

Exchange rates provided by [ExchangeRate-API](https://www.exchangerate-api.com/)
