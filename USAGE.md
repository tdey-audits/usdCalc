# Usage Guide - INR-USD Currency Converter

## Quick Start

### For Linux Users

1. **Download the repository** or clone it:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Run the installer** (recommended):
   ```bash
   ./install.sh
   ```
   This will check dependencies and optionally create a desktop launcher.

3. **Launch the application**:
   ```bash
   ./currency_converter.py
   # or
   ./run.sh
   # or
   python3 currency_converter.py
   ```

## Application Interface

### Main Window

The application features a clean, minimal interface with:

- **Title Area**: "Currency Converter" in red Instrument Serif font
- **USD Input Section**: Enter US Dollar amounts here
- **Conversion Indicator**: Red bidirectional arrow (⇅) showing conversion relationship
- **INR Input Section**: Enter Indian Rupee amounts here
- **Exchange Rate Display**: Shows current exchange rate (live or default)
- **Refresh Button**: Manually update exchange rates
- **Help Text**: Instructions at the bottom

### Color Scheme

- **Background**: Black (#000000)
- **Text**: White (#FFFFFF)
- **Accents/Buttons**: Red (#FF0000)
- **Input Boxes**: Dark background with white text
- **Secondary Text**: Gray (#CCCCCC for info, #666666 for footer)

### Fonts

- **Headings**: Instrument Serif (bold, larger sizes)
- **UI Elements**: Inter (clean, readable)

## How to Use

### Converting Currency

1. **USD to INR**:
   - Click in the USD input field
   - Type the amount (e.g., 100)
   - The INR field automatically updates with the converted amount

2. **INR to USD**:
   - Click in the INR input field
   - Type the amount (e.g., 8312)
   - The USD field automatically updates with the converted amount

3. **Real-time Conversion**:
   - Conversions happen as you type
   - No need to press Enter or click a button
   - Both fields support decimal values

### Refreshing Exchange Rates

- Click the "Refresh Rate" button to fetch the latest exchange rate
- A dialog will confirm successful update or warn if offline
- The rate display at the bottom shows whether you're using a live or default rate

### Exchange Rate Information

The app displays the current exchange rate at the bottom:
- **"1 USD = ₹XX.XX INR (live rate)"** - Successfully fetched from API
- **"1 USD = ₹XX.XX INR (default rate)"** - Using fallback rate (offline or API error)

## Features

### Automatic Rate Fetching

- On startup, the app attempts to fetch the current exchange rate
- Rates are cached for 1 hour to reduce API calls
- Automatically refreshes after cache expires

### Offline Support

- If unable to fetch rates (no internet, API down), uses a default rate
- Continues to work offline with the last cached rate
- Visual indicator shows whether rate is live or default

### Input Validation

- Accepts decimal numbers (e.g., 123.45)
- Handles comma-separated numbers (e.g., 1,234.56)
- Ignores invalid characters automatically
- Clears opposite field when input is empty

### Number Formatting

- Results are formatted with commas for thousands (e.g., 1,234.56)
- Always shows 2 decimal places for precision
- Easy to read at a glance

## Keyboard Shortcuts

- **Tab**: Move between input fields
- **Ctrl+A**: Select all text in current field
- **Ctrl+C**: Copy selected text
- **Ctrl+V**: Paste text
- **Backspace/Delete**: Clear characters

## Examples

### Example 1: Converting $100 to INR
1. Type `100` in the USD field
2. See approximately `₹8,312.00` in the INR field (at rate of 83.12)

### Example 2: Converting ₹5000 to USD
1. Type `5000` in the INR field
2. See approximately `$60.15` in the USD field (at rate of 83.12)

### Example 3: Checking Exchange Rate
1. Look at the bottom of the window
2. Read "1 USD = ₹XX.XX INR (live rate)"
3. This is your current conversion rate

## Troubleshooting

### Application won't start

**Solution**: Check Python installation
```bash
python3 --version  # Should be 3.6 or higher
python3 -c "import tkinter"  # Should not show errors
```

If tkinter is missing:
```bash
sudo apt install python3-tk  # Ubuntu/Debian
```

### Numbers not converting

**Solution**: 
- Make sure you're typing valid numbers
- Try clicking in the field first
- Check that the exchange rate is displayed at the bottom

### "Failed to fetch rate" message

**Solution**: 
- Check your internet connection
- The app will still work with the default/cached rate
- Try clicking "Refresh Rate" when back online

### Fonts look different

**Solution**: 
- The app works with system fonts as fallback
- For best appearance, install Inter and Instrument Serif fonts
- See README.md for font installation instructions

## Tips for Best Experience

1. **Keep it running**: Leave the app open for quick conversions throughout the day
2. **Refresh regularly**: Click "Refresh Rate" if you need the most up-to-date rate
3. **Use decimals**: Enter precise amounts like 99.99 for accurate conversions
4. **Install fonts**: Get Inter and Instrument Serif for the intended design
5. **Create launcher**: Use the install script to add the app to your application menu

## Technical Details

### Exchange Rate API

- Uses exchangerate-api.com for live rates
- Free tier allows sufficient requests for personal use
- No API key required
- Automatic fallback to default rate if unavailable

### Rate Caching

- Rates cached for 1 hour
- Reduces API calls
- Improves responsiveness
- Ensures offline functionality

### Default Rate

- Default: 1 USD = ₹83.12 INR
- Based on approximate average rate
- Used when API is unavailable
- Automatically replaced when live rate is fetched

## Support

For issues, questions, or contributions, please refer to the project repository.

Enjoy converting currencies! 💱
