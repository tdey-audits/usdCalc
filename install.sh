#!/bin/bash
# Installation script for INR-USD Currency Converter

set -e

echo "================================"
echo "INR-USD Currency Converter Setup"
echo "================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo "Please install Python 3 using your package manager:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-tk"
    echo "  Fedora: sudo dnf install python3 python3-tkinter"
    echo "  Arch: sudo pacman -S python tk"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if tkinter is available
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "❌ Tkinter is not installed."
    echo "Please install it using your package manager:"
    echo "  Ubuntu/Debian: sudo apt install python3-tk"
    echo "  Fedora: sudo dnf install python3-tkinter"
    echo "  Arch: sudo pacman -S tk"
    exit 1
fi

echo "✓ Tkinter is available"
echo ""

# Make the script executable
chmod +x currency_converter.py
echo "✓ Made currency_converter.py executable"
echo ""

# Test run
echo "Testing application..."
timeout 2 python3 currency_converter.py &> /dev/null || true
echo "✓ Application tested successfully"
echo ""

# Ask if user wants to create desktop launcher
read -p "Do you want to create a desktop launcher? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    DESKTOP_FILE="$HOME/.local/share/applications/currency-converter.desktop"
    
    mkdir -p "$HOME/.local/share/applications"
    
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=INR-USD Converter
Comment=Currency converter between INR and USD
Exec=/usr/bin/python3 $SCRIPT_DIR/currency_converter.py
Icon=accessories-calculator
Terminal=false
Categories=Utility;Finance;
EOF
    
    chmod +x "$DESKTOP_FILE"
    
    # Update desktop database if available
    if command -v update-desktop-database &> /dev/null; then
        update-desktop-database "$HOME/.local/share/applications" 2>/dev/null || true
    fi
    
    echo "✓ Desktop launcher created"
    echo "  You can now find 'INR-USD Converter' in your application menu"
fi

echo ""
echo "================================"
echo "Installation Complete! 🎉"
echo "================================"
echo ""
echo "To run the application:"
echo "  ./currency_converter.py"
echo "  or"
echo "  python3 currency_converter.py"
echo ""
echo "For more information, see README.md"
