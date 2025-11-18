#!/usr/bin/env python3
"""INR-USD Currency Converter

This module provides both a Tkinter-based GUI application and a command-line
interface (CLI) for converting between Indian Rupees (INR) and US Dollars (USD).
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta

try:
    import tkinter as tk
    from tkinter import messagebox
except ModuleNotFoundError:  # pragma: no cover - depends on system packages
    tk = None
    messagebox = None

__all__ = [
    "CurrencyConverter",
    "ConverterApp",
    "cli_main",
    "run_gui",
    "__version__",
]

__version__ = "1.0.0"


class CurrencyConverter:
    """Business logic for currency conversion and exchange rate caching."""

    def __init__(self) -> None:
        self.exchange_rate = 83.12
        self.last_updated: datetime | None = None
        self.cache_duration = timedelta(hours=1)

    def fetch_exchange_rate(self) -> bool:
        """Fetch the current USD→INR exchange rate from the public API."""
        try:
            url = "https://api.exchangerate-api.com/v4/latest/USD"
            with urllib.request.urlopen(url, timeout=5) as response:
                data = json.loads(response.read().decode())
                self.exchange_rate = float(data["rates"]["INR"])
                self.last_updated = datetime.now()
                return True
        except (
            urllib.error.URLError,
            urllib.error.HTTPError,
            KeyError,
            json.JSONDecodeError,
            ValueError,
        ):
            return False

    def get_exchange_rate(self) -> float:
        """Return the cached exchange rate, fetching a fresh value if needed."""
        if (
            self.last_updated is None
            or datetime.now() - self.last_updated > self.cache_duration
        ):
            self.fetch_exchange_rate()
        return self.exchange_rate

    def usd_to_inr(self, amount: float) -> float:
        """Convert an amount from USD to INR."""
        return amount * self.get_exchange_rate()

    def inr_to_usd(self, amount: float) -> float:
        """Convert an amount from INR to USD."""
        return amount / self.get_exchange_rate()


class ConverterApp:
    """Tkinter GUI application for the currency converter."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.converter = CurrencyConverter()
        self.setup_window()
        self.create_widgets()
        self.fetch_initial_rate()

    def setup_window(self) -> None:
        """Configure the main window properties."""
        self.root.title("INR ⇄ USD Converter")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#000000")

    def create_widgets(self) -> None:
        """Create and layout all Tkinter widgets for the UI."""
        main_frame = tk.Frame(self.root, bg="#000000")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)

        title_label = tk.Label(
            main_frame,
            text="Currency Converter",
            font=("Instrument Serif", 32, "bold"),
            fg="#FF0000",
            bg="#000000",
        )
        title_label.pack(pady=(0, 10))

        subtitle_label = tk.Label(
            main_frame,
            text="INR ⇄ USD",
            font=("Inter", 14),
            fg="#FFFFFF",
            bg="#000000",
        )
        subtitle_label.pack(pady=(0, 30))

        self.create_currency_section(
            main_frame,
            "US Dollar",
            "USD",
            is_usd=True,
        )

        indicator_frame = tk.Frame(main_frame, bg="#000000")
        indicator_frame.pack(pady=20)

        tk.Label(
            indicator_frame,
            text="⇅",
            font=("Inter", 24, "bold"),
            fg="#FF0000",
            bg="#000000",
        ).pack()

        self.create_currency_section(
            main_frame,
            "Indian Rupee",
            "INR",
            is_usd=False,
        )

        self.rate_label = tk.Label(
            main_frame,
            text="",
            font=("Inter", 11),
            fg="#CCCCCC",
            bg="#000000",
        )
        self.rate_label.pack(pady=(30, 10))

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
            command=self.refresh_rate,
        )
        refresh_btn.pack(pady=(0, 20))

        footer_label = tk.Label(
            main_frame,
            text="Enter amount in either field to convert",
            font=("Inter", 10),
            fg="#666666",
            bg="#000000",
        )
        footer_label.pack(side="bottom", pady=(20, 0))

    def create_currency_section(
        self, parent: tk.Frame, currency_name: str, currency_code: str, is_usd: bool
    ) -> None:
        """Create a labelled currency entry section."""
        frame = tk.Frame(parent, bg="#1A1A1A", relief="flat")
        frame.pack(fill="x", pady=10)

        inner_frame = tk.Frame(frame, bg="#1A1A1A")
        inner_frame.pack(padx=20, pady=20)

        label = tk.Label(
            inner_frame,
            text=f"{currency_name} ({currency_code})",
            font=("Instrument Serif", 16, "bold"),
            fg="#FFFFFF",
            bg="#1A1A1A",
        )
        label.pack(anchor="w", pady=(0, 10))

        entry = tk.Entry(
            inner_frame,
            font=("Inter", 20),
            fg="#FFFFFF",
            bg="#000000",
            insertbackground="#FF0000",
            relief="flat",
            justify="left",
            width=20,
        )
        entry.pack(fill="x", ipady=10, ipadx=10)

        if is_usd:
            self.usd_entry = entry
            entry.bind("<KeyRelease>", lambda _event: self.convert_currency("usd"))
        else:
            self.inr_entry = entry
            entry.bind("<KeyRelease>", lambda _event: self.convert_currency("inr"))

    def convert_currency(self, source: str) -> None:
        """Handle conversion when the user types in either field."""
        try:
            if source == "usd":
                amount_str = self.usd_entry.get().strip()
                if not amount_str:
                    self.inr_entry.delete(0, tk.END)
                    return

                amount = float(amount_str.replace(",", ""))
                result = self.converter.usd_to_inr(amount)

                self.inr_entry.delete(0, tk.END)
                self.inr_entry.insert(0, f"{result:,.2f}")

            else:
                amount_str = self.inr_entry.get().strip()
                if not amount_str:
                    self.usd_entry.delete(0, tk.END)
                    return

                amount = float(amount_str.replace(",", ""))
                result = self.converter.inr_to_usd(amount)

                self.usd_entry.delete(0, tk.END)
                self.usd_entry.insert(0, f"{result:,.2f}")

        except ValueError:
            # Ignore invalid intermediate input (e.g., typing "-" or ".")
            pass

    def fetch_initial_rate(self) -> None:
        """Retrieve the initial exchange rate when the app launches."""
        if self.converter.fetch_exchange_rate():
            self.update_rate_display()
        else:
            self.update_rate_display(failed=True)

    def refresh_rate(self) -> None:
        """Manually fetch the latest exchange rate."""
        if self.converter.fetch_exchange_rate():
            self.update_rate_display()
            if self.usd_entry.get():
                self.convert_currency("usd")
            elif self.inr_entry.get():
                self.convert_currency("inr")
            messagebox.showinfo("Success", "Exchange rate updated successfully!")
        else:
            self.update_rate_display(failed=True)
            messagebox.showwarning(
                "Warning", "Failed to fetch rate. Using cached/default rate."
            )

    def update_rate_display(self, failed: bool = False) -> None:
        """Update the label showing the current exchange rate."""
        rate = self.converter.exchange_rate
        if failed:
            self.rate_label.config(
                text=f"1 USD = ₹{rate:.2f} INR (default rate)",
                fg="#FF6666",
            )
        else:
            self.rate_label.config(
                text=f"1 USD = ₹{rate:.2f} INR (live rate)",
                fg="#CCCCCC",
            )


def run_gui() -> None:
    """Launch the Tkinter GUI application."""
    if tk is None:
        print("Error: Tkinter is not available. GUI mode requires Tkinter.")
        print("Please install python3-tk (Debian/Ubuntu) or python3-tkinter (Fedora).")
        sys.exit(1)

    root = tk.Tk()

    try:
        from tkinter import font

        available_fonts = font.families()
        if "Inter" not in available_fonts:
            print("Note: Inter font not found, using default sans-serif")
        if "Instrument Serif" not in available_fonts:
            print("Note: Instrument Serif font not found, using default serif")
    except Exception:
        pass

    app = ConverterApp(root)
    root.mainloop()


def _parse_currency(value: str) -> str:
    lowered = value.lower()
    if lowered not in {"usd", "inr"}:
        raise argparse.ArgumentTypeError(
            "currency must be either 'usd' or 'inr'"
        )
    return lowered


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="inr-usd-converter",
        description="Convert amounts between Indian Rupees (INR) and US Dollars (USD).",
    )
    parser.add_argument(
        "amount",
        nargs="?",
        help="Numeric amount to convert. If omitted, the GUI is launched.",
    )
    parser.add_argument(
        "currency",
        nargs="?",
        type=_parse_currency,
        help="Currency of the provided amount ('usd' or 'inr').",
    )
    parser.add_argument(
        "--rate",
        action="store_true",
        help="Display the current USD→INR exchange rate and exit.",
    )
    parser.add_argument(
        "--no-fetch",
        action="store_true",
        help="Do not attempt to fetch live rates; use the cached/default rate.",
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Force launching the GUI application regardless of other arguments.",
    )
    parser.add_argument(
        "--precision",
        type=int,
        default=2,
        help="Number of decimal places to display in conversion results (default: 2).",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"inr-usd-converter {__version__}",
    )
    return parser


def cli_main(argv: list[str] | None = None) -> int:
    """Entry point for the command-line interface."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.gui or (args.amount is None and not args.rate):
        if tk is None:
            parser.error(
                "Tkinter is not available on this system. Install python3-tk to launch the GUI."
            )
        run_gui()
        return 0

    converter = CurrencyConverter()

    if args.no_fetch:
        converter.last_updated = datetime.now()
        fetched = False
    else:
        fetched = converter.fetch_exchange_rate()

    rate = converter.exchange_rate

    if args.rate:
        status = "live rate" if fetched else "cached/default rate"
        print(f"1 USD = ₹{rate:.2f} INR ({status})")
        return 0

    if args.amount is None or args.currency is None:
        parser.error(
            "amount and currency are required unless --gui or --rate is specified"
        )

    try:
        amount_value = float(args.amount.replace(",", ""))
    except ValueError as exc:  # pragma: no cover - validated by parser.error
        parser.error(f"invalid amount '{args.amount}': {exc}")

    precision = max(0, args.precision)

    if args.currency == "usd":
        converted = converter.usd_to_inr(amount_value)
        print(f"${amount_value:,.{precision}f} USD = ₹{converted:,.{precision}f} INR")
    else:
        converted = converter.inr_to_usd(amount_value)
        print(f"₹{amount_value:,.{precision}f} INR = ${converted:,.{precision}f} USD")

    if fetched:
        print(f"(Live rate: 1 USD = ₹{rate:.2f} INR)")
    else:
        reason = "default rate" if args.no_fetch else "cached/default rate"
        print(f"(Using {reason}: 1 USD = ₹{rate:.2f} INR)")

    return 0


def main() -> None:
    """Console-script entry point bridging to the CLI."""
    sys.exit(cli_main(sys.argv[1:]))


if __name__ == "__main__":
    main()
