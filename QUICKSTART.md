# Quick Start Guide

Get the INR-USD Currency Converter running in 30 seconds!

## Method 1: Homebrew (Recommended)

### macOS or Linux with Homebrew

```bash
# Install via Homebrew
brew tap tdey-audits/tools
brew install inr-usd-converter

# Run CLI
inr-usd-converter 100 usd

# Run GUI
inr-usd-converter-gui
```

**That's it!** 🎉

See [HOMEBREW.md](HOMEBREW.md) for detailed Homebrew instructions.

---

## Method 2: Manual Installation

### For Linux Users

#### Step 1: Clone or Download

```bash
git clone https://github.com/tdey-audits/usdCalc.git
cd usdCalc
```

Or download and extract the ZIP file.

#### Step 2: Run the Installer

```bash
./install.sh
```

This will:
- Check if Python 3 and Tkinter are installed
- Make the app executable
- Optionally create a desktop launcher

#### Step 3: Launch the App

**GUI Mode:**
```bash
./currency_converter.py
```

Or use the launcher:
```bash
./run.sh
```

Or find "INR-USD Converter" in your application menu (if you created the desktop launcher).

**CLI Mode:**
```bash
./currency_converter.py 100 usd
./currency_converter.py 5000 inr
./currency_converter.py --help
```

---

## Usage Examples

### Command Line

```bash
# Convert 100 USD to INR
inr-usd-converter 100 usd

# Convert 5000 INR to USD
inr-usd-converter 5000 inr

# Check current exchange rate
inr-usd-converter --rate

# Show help
inr-usd-converter --help
```

### Graphical Interface

- Type a number in either the USD or INR field
- See the conversion instantly
- Click "Refresh Rate" to update the exchange rate

---

## Troubleshooting

### If you get "Python not found"
```bash
# Ubuntu/Debian
sudo apt install python3 python3-tk

# Fedora
sudo dnf install python3 python3-tkinter

# Arch
sudo pacman -S python tk

# macOS with Homebrew
brew install python@3.11
```

### If the GUI won't start

**Check Tkinter:**
```bash
python3 -c "import tkinter; print('Tkinter is available')"
```

**Install if missing:**
```bash
sudo apt install python3-tk  # Debian/Ubuntu
brew reinstall python@3.11   # macOS
```

### If fonts look wrong

The app works fine with system fonts. For the best visual experience, install Inter and Instrument Serif fonts (see README.md for details).

### Command not found (Homebrew)

Add Homebrew to your PATH:
```bash
# Linux
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# macOS
export PATH="/usr/local/bin:$PATH"  # Intel
export PATH="/opt/homebrew/bin:$PATH"  # Apple Silicon
```

---

## Need More Help?

- **Homebrew installation**: See [HOMEBREW.md](HOMEBREW.md)
- **Installation details**: See [README.md](README.md)
- **Usage guide**: See [USAGE.md](USAGE.md)
- **Features & design**: See [FEATURES.md](FEATURES.md)

---

## Quick Examples

**Convert $100 to INR:**
1. Type `100` in the USD field (GUI) or run `inr-usd-converter 100 usd` (CLI)
2. See the result instantly (e.g., ₹8,312.00)

**Convert ₹5000 to USD:**
1. Type `5000` in the INR field (GUI) or run `inr-usd-converter 5000 inr` (CLI)
2. See the result instantly (e.g., $60.15)

**Check Exchange Rate:**
```bash
inr-usd-converter --rate
# Output: 1 USD = ₹83.12 INR (live rate)
```

Enjoy! 💱
