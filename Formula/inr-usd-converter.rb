require "language/python/virtualenv"

class InrUsdConverter < Formula
  include Language::Python::Virtualenv

  desc "INR ⇄ USD currency converter with CLI and GUI interfaces"
  homepage "https://github.com/tdey-audits/usdCalc"
  url "https://github.com/tdey-audits/usdCalc/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "faa1204e9d4f63b5baced8e72072635ee5eab038958202876b5c26a9733a52ad"
  license "MIT"
  head "https://github.com/tdey-audits/usdCalc.git", branch: "main"

  depends_on "python@3.11"

  def install
    virtualenv_install_with_resources

    if OS.linux? && (buildpath/"resources/inr-usd-converter.desktop").exist?
      (share/"applications").install buildpath/"resources/inr-usd-converter.desktop"
      inreplace share/"applications/inr-usd-converter.desktop", "Exec=inr-usd-converter-gui", "Exec=#{bin}/inr-usd-converter-gui"
    end
  end

  def caveats
    s = <<~EOS
      The INR-USD Converter has been installed with both CLI and GUI interfaces.

      CLI Usage:
        inr-usd-converter 100 usd          # Convert 100 USD to INR
        inr-usd-converter 1000 inr         # Convert 1000 INR to USD
        inr-usd-converter --rate           # Display current exchange rate
        inr-usd-converter --help           # Show all CLI options

      GUI Usage:
        inr-usd-converter-gui              # Launch the Tkinter GUI application
        inr-usd-converter                  # With no arguments, also launches GUI

    EOS

    if OS.mac?
      s += <<~EOS
        Note: On macOS, Tkinter should be available by default with Homebrew Python.
        If the GUI doesn't work, ensure you have the full Python installation:
          brew reinstall python@3.11

      EOS
    else
      s += <<~EOS
        Note: On Linux, you may need to install python3-tk for GUI functionality:
          sudo apt install python3-tk       # Debian/Ubuntu
          sudo dnf install python3-tkinter  # Fedora
          sudo pacman -S tk                 # Arch Linux

        A desktop launcher has been installed to: #{HOMEBREW_PREFIX}/share/applications/

      EOS
    end
    s
  end

  test do
    assert_match "1 USD", shell_output("#{bin}/inr-usd-converter --rate --no-fetch")
    assert_match "INR", shell_output("#{bin}/inr-usd-converter 100 usd --no-fetch")
    assert_match "USD", shell_output("#{bin}/inr-usd-converter 1000 inr --no-fetch")
    assert_match version.to_s, shell_output("#{bin}/inr-usd-converter --version")
  end
end
