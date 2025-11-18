#!/usr/bin/env python3
"""
INR-USD Currency Converter
A standalone application for converting between Indian Rupees and US Dollars
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from typing import Optional

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


class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.converter = CurrencyConverter()
        self.setup_window()
        self.create_widgets()
        self.fetch_initial_rate()
        
    def setup_window(self):
        """Configure main window"""
        self.root.title("INR ⇄ USD Converter")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#000000")
        
    def create_widgets(self):
        """Create all UI widgets"""
        # Main container
        main_frame = tk.Frame(self.root, bg="#000000")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Currency Converter",
            font=("Instrument Serif", 32, "bold"),
            fg="#FF0000",
            bg="#000000"
        )
        title_label.pack(pady=(0, 10))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="INR ⇄ USD",
            font=("Inter", 14),
            fg="#FFFFFF",
            bg="#000000"
        )
        subtitle_label.pack(pady=(0, 30))
        
        # USD Section
        self.create_currency_section(
            main_frame,
            "US Dollar",
            "USD",
            is_usd=True
        )
        
        # Conversion indicator
        indicator_frame = tk.Frame(main_frame, bg="#000000")
        indicator_frame.pack(pady=20)
        
        tk.Label(
            indicator_frame,
            text="⇅",
            font=("Inter", 24, "bold"),
            fg="#FF0000",
            bg="#000000"
        ).pack()
        
        # INR Section
        self.create_currency_section(
            main_frame,
            "Indian Rupee",
            "INR",
            is_usd=False
        )
        
        # Exchange rate info
        self.rate_label = tk.Label(
            main_frame,
            text="",
            font=("Inter", 11),
            fg="#CCCCCC",
            bg="#000000"
        )
        self.rate_label.pack(pady=(30, 10))
        
        # Refresh button
        refresh_btn = tk.Button(
            main_frame,
            text="Refresh Rate",
            font=("Inter", 11, "bold"),
            fg="#FFFFFF",
            bg="#FF0000",
            activeforeground="#FFFFFF",
            activebackground="#CC0000",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8,
            command=self.refresh_rate
        )
        refresh_btn.pack(pady=(0, 20))
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Enter amount in either field to convert",
            font=("Inter", 10),
            fg="#666666",
            bg="#000000"
        )
        footer_label.pack(side="bottom", pady=(20, 0))
        
    def create_currency_section(self, parent, currency_name, currency_code, is_usd):
        """Create a currency input section"""
        frame = tk.Frame(parent, bg="#1A1A1A", relief="flat")
        frame.pack(fill="x", pady=10)
        
        # Inner padding frame
        inner_frame = tk.Frame(frame, bg="#1A1A1A")
        inner_frame.pack(padx=20, pady=20)
        
        # Currency label
        label = tk.Label(
            inner_frame,
            text=f"{currency_name} ({currency_code})",
            font=("Instrument Serif", 16, "bold"),
            fg="#FFFFFF",
            bg="#1A1A1A"
        )
        label.pack(anchor="w", pady=(0, 10))
        
        # Entry field
        entry = tk.Entry(
            inner_frame,
            font=("Inter", 20),
            fg="#FFFFFF",
            bg="#000000",
            insertbackground="#FF0000",
            relief="flat",
            justify="left",
            width=20
        )
        entry.pack(fill="x", ipady=10, ipadx=10)
        
        # Store references
        if is_usd:
            self.usd_entry = entry
            entry.bind("<KeyRelease>", lambda e: self.convert_currency("usd"))
        else:
            self.inr_entry = entry
            entry.bind("<KeyRelease>", lambda e: self.convert_currency("inr"))
            
    def convert_currency(self, source):
        """Handle conversion when user types"""
        try:
            if source == "usd":
                amount_str = self.usd_entry.get().strip()
                if not amount_str or amount_str == "":
                    self.inr_entry.delete(0, tk.END)
                    return
                    
                amount = float(amount_str.replace(",", ""))
                result = self.converter.usd_to_inr(amount)
                
                # Update INR field without triggering its callback
                self.inr_entry.delete(0, tk.END)
                self.inr_entry.insert(0, f"{result:,.2f}")
                
            else:  # source == "inr"
                amount_str = self.inr_entry.get().strip()
                if not amount_str or amount_str == "":
                    self.usd_entry.delete(0, tk.END)
                    return
                    
                amount = float(amount_str.replace(",", ""))
                result = self.converter.inr_to_usd(amount)
                
                # Update USD field without triggering its callback
                self.usd_entry.delete(0, tk.END)
                self.usd_entry.insert(0, f"{result:,.2f}")
                
        except ValueError:
            pass
    
    def fetch_initial_rate(self):
        """Fetch exchange rate on startup"""
        if self.converter.fetch_exchange_rate():
            self.update_rate_display()
        else:
            self.update_rate_display(failed=True)
    
    def refresh_rate(self):
        """Manually refresh exchange rate"""
        if self.converter.fetch_exchange_rate():
            self.update_rate_display()
            # Reconvert if there's a value
            if self.usd_entry.get():
                self.convert_currency("usd")
            elif self.inr_entry.get():
                self.convert_currency("inr")
            messagebox.showinfo("Success", "Exchange rate updated successfully!")
        else:
            self.update_rate_display(failed=True)
            messagebox.showwarning("Warning", "Failed to fetch rate. Using cached/default rate.")
    
    def update_rate_display(self, failed=False):
        """Update the exchange rate display"""
        rate = self.converter.exchange_rate
        if failed:
            self.rate_label.config(
                text=f"1 USD = ₹{rate:.2f} INR (default rate)",
                fg="#FF6666"
            )
        else:
            self.rate_label.config(
                text=f"1 USD = ₹{rate:.2f} INR (live rate)",
                fg="#CCCCCC"
            )


def main():
    root = tk.Tk()
    
    # Try to set fonts (fallback to defaults if custom fonts not available)
    try:
        from tkinter import font
        available_fonts = font.families()
        
        # Check if fonts are available, otherwise use fallbacks
        if "Inter" not in available_fonts:
            print("Note: Inter font not found, using default sans-serif")
        if "Instrument Serif" not in available_fonts:
            print("Note: Instrument Serif font not found, using default serif")
    except:
        pass
    
    app = ConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
