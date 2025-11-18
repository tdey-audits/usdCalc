# Command Line Interface (CLI) Guide

Complete guide to using the INR-USD Converter from the command line.

## Installation

### Via Homebrew
```bash
brew install inr-usd-converter
```

### Via pip (from source)
```bash
pip install .
```

### Manual
```bash
chmod +x currency_converter.py
./currency_converter.py --help
```

## Basic Usage

### Converting Currencies

**USD to INR:**
```bash
inr-usd-converter 100 usd
# Output: $100.00 USD = ₹8,312.00 INR
#         (Live rate: 1 USD = ₹83.12 INR)
```

**INR to USD:**
```bash
inr-usd-converter 5000 inr
# Output: ₹5,000.00 INR = $60.14 USD
#         (Live rate: 1 USD = ₹83.12 INR)
```

### Checking Exchange Rate

```bash
inr-usd-converter --rate
# Output: 1 USD = ₹83.12 INR (live rate)
```

### Decimal Amounts

```bash
inr-usd-converter 50.50 usd
# Output: $50.50 USD = ₹4,197.56 INR
```

### With Commas

```bash
inr-usd-converter 1,234.56 usd
# Output: $1,234.56 USD = ₹102,625.79 INR
```

## Options

### `--help`
Display help information and exit.

```bash
inr-usd-converter --help
```

### `--version`
Show version number and exit.

```bash
inr-usd-converter --version
# Output: inr-usd-converter 1.0.0
```

### `--rate`
Display the current exchange rate without performing a conversion.

```bash
inr-usd-converter --rate
# Output: 1 USD = ₹83.12 INR (live rate)
```

### `--no-fetch`
Use cached or default exchange rate instead of fetching a live rate.

```bash
inr-usd-converter 100 usd --no-fetch
# Output: $100.00 USD = ₹8,312.00 INR
#         (Using default rate: 1 USD = ₹83.12 INR)
```

**Use cases:**
- Working offline
- Avoiding API rate limits
- Faster execution (no network delay)
- Testing with known rates

### `--precision N`
Set the number of decimal places to display (default: 2).

```bash
inr-usd-converter 100 usd --precision 4
# Output: $100.0000 USD = ₹8,312.0000 INR

inr-usd-converter 100 usd --precision 0
# Output: $100 USD = ₹8,312 INR
```

### `--gui`
Force launch the GUI application, ignoring other arguments.

```bash
inr-usd-converter --gui
```

This is equivalent to:
```bash
inr-usd-converter-gui
```

## Advanced Examples

### Scripting

**Convert multiple amounts:**
```bash
for amount in 10 50 100 500 1000; do
  inr-usd-converter $amount usd --no-fetch
done
```

**Check if rate has changed:**
```bash
old_rate=$(cat last_rate.txt 2>/dev/null || echo "0")
new_rate=$(inr-usd-converter --rate | grep -oP '[\d.]+')
echo "$new_rate" > last_rate.txt

if [ "$old_rate" != "$new_rate" ]; then
  echo "Exchange rate changed from ₹$old_rate to ₹$new_rate"
fi
```

**Create a conversion table:**
```bash
#!/bin/bash
echo "USD    INR"
echo "---    ---"
for usd in 10 20 50 100 200 500 1000; do
  inr=$(inr-usd-converter $usd usd --no-fetch | grep -oP '₹[\d,]+' | cut -d₹ -f2)
  printf "%-6s ₹%s\n" "\$$usd" "$inr"
done
```

### Piping and Parsing

**Extract only the converted amount:**
```bash
# Using grep and cut
inr-usd-converter 100 usd | head -1 | grep -oP '₹[\d,.]+'
# Output: ₹8,312.00

# Using awk
inr-usd-converter 100 usd | awk 'NR==1 {print $5}'
# Output: ₹8,312.00
```

**Extract the exchange rate:**
```bash
inr-usd-converter --rate | grep -oP '[\d.]+ INR' | cut -d' ' -f1
# Output: 83.12
```

### Environment-Based Configuration

Create a wrapper script with custom defaults:

```bash
#!/bin/bash
# my-converter.sh - Custom wrapper with defaults

PRECISION=${PRECISION:-2}
NO_FETCH=${NO_FETCH:-false}

if [ "$NO_FETCH" = "true" ]; then
  inr-usd-converter "$@" --precision "$PRECISION" --no-fetch
else
  inr-usd-converter "$@" --precision "$PRECISION"
fi
```

Usage:
```bash
chmod +x my-converter.sh
PRECISION=4 ./my-converter.sh 100 usd
NO_FETCH=true ./my-converter.sh 100 usd
```

## Exit Codes

- **0**: Success
- **1**: Error (invalid arguments, parsing error, etc.)
- **2**: Usage error (from argparse)

Check exit codes in scripts:
```bash
if inr-usd-converter 100 usd > /dev/null; then
  echo "Conversion successful"
else
  echo "Conversion failed"
fi
```

## Output Format

### Conversion Output
```
$<amount> USD = ₹<converted> INR
(<rate_status>)
```

Where `<rate_status>` is one of:
- `Live rate: 1 USD = ₹XX.XX INR` - Successfully fetched from API
- `Using default rate: 1 USD = ₹XX.XX INR` - Using fallback rate with `--no-fetch`
- `Using cached/default rate: 1 USD = ₹XX.XX INR` - API fetch failed

### Rate-Only Output
```
1 USD = ₹<rate> INR (<status>)
```

Where `<status>` is either `live rate` or `cached/default rate`.

## Integration Examples

### Shell Alias

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# Quick conversions
alias usd2inr='inr-usd-converter'
alias inr2usd='inr-usd-converter'
alias exrate='inr-usd-converter --rate'

# Offline conversions
alias usd2inr-offline='inr-usd-converter --no-fetch'
```

Usage:
```bash
usd2inr 100 usd
inr2usd 5000 inr
exrate
```

### Shell Function

```bash
# Add to ~/.bashrc
convert() {
  if [ $# -eq 1 ]; then
    # Assume USD if only amount is given
    inr-usd-converter "$1" usd
  else
    inr-usd-converter "$@"
  fi
}
```

Usage:
```bash
convert 100        # Assumes USD
convert 5000 inr   # Explicit currency
```

### Python Script Integration

```python
import subprocess
import json

def convert_currency(amount, from_currency):
    result = subprocess.run(
        ['inr-usd-converter', str(amount), from_currency.lower(), '--no-fetch'],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        output = result.stdout.strip().split('\n')[0]
        # Parse the output
        print(output)
        return output
    else:
        print(f"Error: {result.stderr}")
        return None

# Example usage
convert_currency(100, 'USD')
convert_currency(5000, 'INR')
```

## Performance Tips

1. **Use `--no-fetch` for repeated conversions** to avoid API rate limits and network delays:
   ```bash
   inr-usd-converter 100 usd --no-fetch
   ```

2. **Cache the rate manually** if doing many conversions:
   ```bash
   rate=$(inr-usd-converter --rate | grep -oP '[\d.]+' | head -1)
   # Use this rate for calculations without making new API calls
   ```

3. **Batch conversions** in a single script to minimize overhead:
   ```bash
   for amount in "${amounts[@]}"; do
     inr-usd-converter "$amount" usd --no-fetch
   done
   ```

## Troubleshooting

### Command Not Found

```bash
# Check if installed
which inr-usd-converter

# If not found, check Homebrew path
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"  # Linux
export PATH="/usr/local/bin:$PATH"                 # macOS

# Or use direct path
python3 /path/to/currency_converter.py 100 usd
```

### Rate Fetch Failures

If you consistently see "cached/default rate" messages:

1. **Check internet connection:**
   ```bash
   ping -c 1 api.exchangerate-api.com
   ```

2. **Check API status:**
   ```bash
   curl https://api.exchangerate-api.com/v4/latest/USD
   ```

3. **Use offline mode explicitly:**
   ```bash
   inr-usd-converter 100 usd --no-fetch
   ```

### Invalid Arguments

```bash
# Wrong: currency before amount
inr-usd-converter usd 100  # Error

# Correct: amount before currency
inr-usd-converter 100 usd

# Wrong: missing currency
inr-usd-converter 100  # Launches GUI instead

# Correct: specify currency
inr-usd-converter 100 usd
```

## Differences from GUI

| Feature | CLI | GUI |
|---------|-----|-----|
| Conversion | One-shot | Real-time |
| Rate updates | Per-invocation | Cached + manual refresh |
| Precision | Configurable | Fixed at 2 decimals |
| Batch operations | Easy with scripts | Not supported |
| Visual feedback | Text output | Interactive fields |
| Offline mode | `--no-fetch` flag | Automatic fallback |

## See Also

- [README.md](README.md) - General documentation
- [USAGE.md](USAGE.md) - GUI usage guide
- [HOMEBREW.md](HOMEBREW.md) - Homebrew installation
- [FEATURES.md](FEATURES.md) - Feature overview

## Support

For CLI-related issues:
- Ensure you're using Python 3.8+
- Check command syntax with `--help`
- Verify currency codes are 'usd' or 'inr' (case-insensitive)
- Use `--no-fetch` if API access is problematic
