#!/usr/bin/env python3
"""Tests for the Currency Converter

This script includes unit tests for the CurrencyConverter class
and integration tests for the CLI.
"""

import sys
from datetime import datetime

try:
    from currency_converter import CurrencyConverter, cli_main
except ImportError:
    sys.path.insert(0, ".")
    from currency_converter import CurrencyConverter, cli_main


def test_converter_logic() -> bool:
    """Test basic conversion functionality."""
    converter = CurrencyConverter()
    converter.exchange_rate = 80.0
    converter.last_updated = datetime.now()

    print("Testing Currency Converter...")
    print(f"Exchange rate: 1 USD = ₹{converter.exchange_rate}")
    print()

    usd_amount = 100
    inr_result = converter.usd_to_inr(usd_amount)
    print(f"✓ USD to INR: ${usd_amount} = ₹{inr_result:.2f}")
    assert inr_result == 8000.0, f"Expected 8000.0, got {inr_result}"

    inr_amount = 8000
    usd_result = converter.inr_to_usd(inr_amount)
    print(f"✓ INR to USD: ₹{inr_amount} = ${usd_result:.2f}")
    assert usd_result == 100.0, f"Expected 100.0, got {usd_result}"

    usd_decimal = 50.50
    inr_decimal_result = converter.usd_to_inr(usd_decimal)
    print(f"✓ Decimal USD to INR: ${usd_decimal} = ₹{inr_decimal_result:.2f}")
    assert inr_decimal_result == 4040.0, f"Expected 4040.0, got {inr_decimal_result}"

    small_usd = 1
    small_inr_result = converter.usd_to_inr(small_usd)
    print(f"✓ Small amount: ${small_usd} = ₹{small_inr_result:.2f}")
    assert small_inr_result == 80.0, f"Expected 80.0, got {small_inr_result}"

    zero_result = converter.usd_to_inr(0)
    print(f"✓ Zero amount: $0 = ₹{zero_result:.2f}")
    assert zero_result == 0.0, f"Expected 0.0, got {zero_result}"

    print()
    print("All conversion tests passed! ✓")
    print()

    print("Testing API fetch...")
    if converter.fetch_exchange_rate():
        print(f"✓ Successfully fetched rate: 1 USD = ₹{converter.exchange_rate:.2f}")
        print("  (This is a live rate from the API)")
    else:
        print("⚠ Could not fetch rate from API (offline or API unavailable)")
        print("  This is normal if you're offline")

    return True


def test_cli() -> bool:
    """Test the CLI interface."""
    print()
    print("Testing CLI interface...")
    print()

    import io
    from contextlib import redirect_stdout

    test_cases = [
        (["--rate", "--no-fetch"], "rate display"),
        (["100", "usd", "--no-fetch"], "USD to INR conversion"),
        (["1000", "inr", "--no-fetch"], "INR to USD conversion"),
        (["50.50", "usd", "--no-fetch", "--precision", "3"], "precision argument"),
    ]

    for args, description in test_cases:
        print(f"Testing {description}...")
        f = io.StringIO()
        try:
            with redirect_stdout(f):
                result = cli_main(args)
            output = f.getvalue()
            assert result == 0, f"CLI returned non-zero exit code for {description}"
            assert output.strip(), f"CLI produced no output for {description}"
            print(f"✓ {description} works")
        except SystemExit as e:
            if e.code != 0:
                raise AssertionError(
                    f"CLI exited with code {e.code} for {description}"
                )
            output = f.getvalue()
            print(f"✓ {description} works")

    print()
    print("All CLI tests passed! ✓")
    return True


if __name__ == "__main__":
    try:
        success = test_converter_logic()
        success = test_cli() and success
        print()
        print("=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
