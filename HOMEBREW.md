# Homebrew Installation Guide

This guide covers installing the INR-USD Currency Converter via Homebrew/Linuxbrew on both macOS and Linux systems.

## Prerequisites

### macOS

Homebrew should already be installed on most macOS systems. If not:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Linux (Linuxbrew)

Install Homebrew on Linux:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installation, add Homebrew to your PATH:

```bash
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```

## Installation

### From Official Tap (Recommended)

Once the formula is published to a tap, install with:

```bash
brew tap tdey-audits/tools
brew install inr-usd-converter
```

### From Local Formula (Development)

To test the formula locally:

```bash
# Clone the repository
git clone https://github.com/tdey-audits/usdCalc.git
cd usdCalc

# Install using the local formula
brew install --build-from-source Formula/inr-usd-converter.rb
```

### Installing as a Development Version

```bash
# Install from the HEAD (latest commit)
brew install --HEAD inr-usd-converter
```

## Post-Installation

### Verify Installation

```bash
# Check version
inr-usd-converter --version

# Test CLI
inr-usd-converter 100 usd --no-fetch

# Test GUI (if Tkinter is available)
inr-usd-converter-gui
```

### Linux: GUI Requirements

On Linux, you may need to install Tkinter separately for GUI functionality:

```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk

# openSUSE
sudo zypper install python3-tk
```

### macOS: GUI Requirements

Tkinter should be available by default with Homebrew's Python. If you encounter issues:

```bash
brew reinstall python@3.11
```

## Usage

### Command Line Interface

```bash
# Convert currencies
inr-usd-converter 100 usd
inr-usd-converter 5000 inr

# Check exchange rate
inr-usd-converter --rate

# Show help
inr-usd-converter --help
```

### Graphical Interface

```bash
# Launch GUI
inr-usd-converter-gui

# Or launch without arguments
inr-usd-converter
```

### Desktop Integration (Linux)

After installation, the application should appear in your application menu under:
- **Categories**: Utility → Finance or Office → Finance
- **Name**: INR-USD Converter

The desktop entry is installed to: `$HOMEBREW_PREFIX/share/applications/`

If it doesn't appear, you can update your desktop database:

```bash
update-desktop-database ~/.local/share/applications/
# or
update-desktop-database /home/linuxbrew/.linuxbrew/share/applications/
```

## Updating

```bash
# Update Homebrew
brew update

# Upgrade the application
brew upgrade inr-usd-converter
```

## Uninstallation

```bash
brew uninstall inr-usd-converter
```

On Linux, this will also remove the desktop entry.

## Troubleshooting

### Command Not Found

If `inr-usd-converter` is not found after installation:

```bash
# Check if Homebrew's bin is in your PATH
echo $PATH | grep brew

# If not, add it:
# For Linux:
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# For macOS (Intel):
export PATH="/usr/local/bin:$PATH"

# For macOS (Apple Silicon):
export PATH="/opt/homebrew/bin:$PATH"
```

### GUI Won't Launch on Linux

Install Tkinter:

```bash
sudo apt install python3-tk  # Debian/Ubuntu
```

Verify Tkinter is available:

```bash
python3 -c "import tkinter; print('Tkinter is available')"
```

### Fonts Not Displaying Properly

The application uses Inter and Instrument Serif fonts. If they're not available, it falls back to system fonts. To install them:

**Ubuntu/Debian:**
```bash
sudo apt install fonts-inter
```

For Instrument Serif, download from [Google Fonts](https://fonts.google.com/specimen/Instrument+Serif).

**macOS:**
```bash
brew tap homebrew/cask-fonts
brew install --cask font-inter
brew install --cask font-instrument-serif
```

### API Rate Limit Issues

The free ExchangeRate-API tier has limits. If you hit rate limits:

```bash
# Use the --no-fetch flag to avoid API calls
inr-usd-converter 100 usd --no-fetch
```

The application caches rates for 1 hour, so this should rarely be an issue.

## Building from Source

If you want to modify the formula or build from source:

```bash
# Clone the repository
git clone https://github.com/tdey-audits/usdCalc.git
cd usdCalc

# Edit the formula if needed
vim Formula/inr-usd-converter.rb

# Install with --build-from-source
brew install --build-from-source ./Formula/inr-usd-converter.rb

# Or for development
brew install --HEAD --build-from-source ./Formula/inr-usd-converter.rb
```

## Formula Maintenance

### Creating a Release

1. Tag a new version:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

2. Create a tarball:
   ```bash
   git archive --format=tar.gz --prefix=inr-usd-converter-1.0.0/ v1.0.0 > inr-usd-converter-1.0.0.tar.gz
   ```

3. Calculate SHA256:
   ```bash
   shasum -a 256 inr-usd-converter-1.0.0.tar.gz
   ```

4. Update the formula's `sha256` value with the calculated hash.

### Testing the Formula

```bash
# Audit the formula
brew audit --strict Formula/inr-usd-converter.rb

# Test installation
brew install --build-from-source Formula/inr-usd-converter.rb

# Run tests
brew test inr-usd-converter
```

## Additional Resources

- **GitHub Repository**: https://github.com/tdey-audits/usdCalc
- **Homebrew Documentation**: https://docs.brew.sh/
- **Python on Homebrew**: https://docs.brew.sh/Homebrew-and-Python

## Support

For issues specific to the Homebrew installation:

1. Check if the issue exists with manual installation
2. Verify Homebrew is up to date: `brew update`
3. Check formula audit: `brew audit inr-usd-converter`
4. Report issues to the GitHub repository

For general usage issues, see [README.md](README.md) and [USAGE.md](USAGE.md).
