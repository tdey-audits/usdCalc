# Quick Start Guide

Get the INR-USD Currency Converter running in 30 seconds!

## For Linux Users

### Step 1: Clone or Download

```bash
git clone <repository-url>
cd inr-usd-converter
```

Or download and extract the ZIP file.

### Step 2: Run the Installer

```bash
./install.sh
```

This will:
- Check if Python 3 and Tkinter are installed
- Make the app executable
- Optionally create a desktop launcher

### Step 3: Launch the App

```bash
./currency_converter.py
```

Or use the launcher:
```bash
./run.sh
```

Or find "INR-USD Converter" in your application menu (if you created the desktop launcher).

## That's It! 🎉

- Type a number in either the USD or INR field
- See the conversion instantly
- Click "Refresh Rate" to update the exchange rate

## Troubleshooting

### If you get "Python not found"
```bash
# Ubuntu/Debian
sudo apt install python3 python3-tk

# Fedora
sudo dnf install python3 python3-tkinter

# Arch
sudo pacman -S python tk
```

### If the app won't start
```bash
# Try running directly with Python
python3 currency_converter.py

# Check Python version (needs 3.6+)
python3 --version
```

### If fonts look wrong
The app works fine with system fonts. For the best visual experience, install Inter and Instrument Serif fonts (see README.md for details).

## Need More Help?

- **Installation details**: See [README.md](README.md)
- **Usage guide**: See [USAGE.md](USAGE.md)
- **Features & design**: See [FEATURES.md](FEATURES.md)

## Examples

**Convert $100 to INR:**
1. Type `100` in the USD field
2. See the result instantly in the INR field (e.g., ₹8,312.00)

**Convert ₹5000 to USD:**
1. Type `5000` in the INR field
2. See the result instantly in the USD field (e.g., $60.15)

Enjoy! 💱
