# 🌍 ipGEO CLI

A sleek, interactive command-line tool built in Python to geolocate IP addresses and visualize them on a 3D ASCII globe directly in your terminal.

## 🚀 Features
- **Instant Geolocation**: Fetch city, region, country, and organization data using `ipinfo.io`.
- **ASCII Visuals**: Beautifully formatted tables and panels using the [Rich](https://github.com) library.
- **Interactive 3D Globe**: Launches an interactive ASCII Earth pinned at the target coordinates.
- **Orbital Animation**: A "hacker-style" loading sequence before displaying data.

## 🛠️ Prerequisites
Before running the script, ensure you have the following system tools installed:

1. **Python 3.x**
2. **Curl**: Used for network requests.
3. **Globe-CLI**: The 3D ASCII renderer.
   ```bash
   # Install via Cargo (Rust)
   cargo install globe-cli
## How to get
1. clone and install requirments
   ```bash
   git clone https://github.com
   cd ip-geo
   pip install rich requests
## RUN
python ipGEO.py

