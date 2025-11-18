#!/usr/bin/env python3
"""
Simple tests for the Currency Converter
Run with: python3 test_converter.py
"""

import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta

# Import only the converter logic, not the GUI
class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = 83.12
        self.last_updated = None
        self.cache_duration = timedelta(hours=1)
        
    def fetch_exchange_rate(self) -> bool:
        """Fetch current exchange rate from API"""
        try:
            url = "https://api.exchangerate-api.com/v4/latest/USD"
            with urllib.request.urlopen(url, timeout=5) as response:
                data = json.loads(response.read().decode())
                self.exchange_rate = data['rates']['INR']
                self.last_updated = datetime.now()
                return True
        except (urllib.error.URLError, urllib.error.HTTPError, KeyError, json.JSONDecodeError):
            return False
    
    def get_exchange_rate(self) -> float:
        """Get exchange rate, fetching if cache is stale"""
        if self.last_updated is None or datetime.now() - self.last_updated > self.cache_duration:
            self.fetch_exchange_rate()
        return self.exchange_rate
    
    def usd_to_inr(self, amount: float) -> float:
        """Convert USD to INR"""
        return amount * self.get_exchange_rate()
    
    def inr_to_usd(self, amount: float) -> float:
        """Convert INR to USD"""
        return amount / self.get_exchange_rate()


def test_converter():
    """Test basic conversion functionality"""
    converter = CurrencyConverter()
    
    # Set a known exchange rate for testing and mark as updated to prevent auto-fetch
    converter.exchange_rate = 80.0
    converter.last_updated = datetime.now()
    
    print("Testing Currency Converter...")
    print(f"Exchange rate: 1 USD = ₹{converter.exchange_rate}")
    print()
    
    # Test USD to INR
    usd_amount = 100
    inr_result = converter.usd_to_inr(usd_amount)
    print(f"✓ USD to INR: ${usd_amount} = ₹{inr_result:.2f}")
    assert inr_result == 8000.0, f"Expected 8000.0, got {inr_result}"
    
    # Test INR to USD
    inr_amount = 8000
    usd_result = converter.inr_to_usd(inr_amount)
    print(f"✓ INR to USD: ₹{inr_amount} = ${usd_result:.2f}")
    assert usd_result == 100.0, f"Expected 100.0, got {usd_result}"
    
    # Test decimal amounts
    usd_decimal = 50.50
    inr_decimal_result = converter.usd_to_inr(usd_decimal)
    print(f"✓ Decimal USD to INR: ${usd_decimal} = ₹{inr_decimal_result:.2f}")
    assert inr_decimal_result == 4040.0, f"Expected 4040.0, got {inr_decimal_result}"
    
    # Test small amounts
    small_usd = 1
    small_inr_result = converter.usd_to_inr(small_usd)
    print(f"✓ Small amount: ${small_usd} = ₹{small_inr_result:.2f}")
    assert small_inr_result == 80.0, f"Expected 80.0, got {small_inr_result}"
    
    # Test zero
    zero_result = converter.usd_to_inr(0)
    print(f"✓ Zero amount: $0 = ₹{zero_result:.2f}")
    assert zero_result == 0.0, f"Expected 0.0, got {zero_result}"
    
    print()
    print("All tests passed! ✓")
    print()
    
    # Test API fetch (informational)
    print("Testing API fetch...")
    if converter.fetch_exchange_rate():
        print(f"✓ Successfully fetched rate: 1 USD = ₹{converter.exchange_rate:.2f}")
        print("  (This is a live rate from the API)")
    else:
        print("⚠ Could not fetch rate from API (offline or API unavailable)")
        print("  This is normal if you're offline")
    
    return True


if __name__ == "__main__":
    try:
        success = test_converter()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        sys.exit(1)
