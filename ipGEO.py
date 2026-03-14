  #GNU nano 8.6                                            ipGEO.py
import argparse
import subprocess
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

parser = argparse.ArgumentParser(description="ipGEO CLI")
parser.add_argument("-t", "--target", help="target ip.")
args = parser.parse_args()

c = Console()
target = args.target or c.input("[bold cyan]Enter target IP: [/bold cyan]")

# Run curl and capture the output into a variable
result = subprocess.run(
    ["curl", "-s", f"ipinfo.io/{target}/json"],
    capture_output=True,
    text=True
)


# Convert the text string into a Python dictionary (data)
try:
    data = json.loads(result.stdout)
except json.JSONDecodeError:
   c.print("[bold red]Error: Could not retrieve data. Check your connection or IP address.[/bold red]")
   exit()

# Build the table using the 'data' dictionary
table = Table(title=f"GeoIP Report: {data.get('ip')}", show_header=True, header_style="bold magenta")
table.add_column("Attribute", style="cyan")
table.add_column("Value", style="white")

fields = ["hostname", "city", "region", "country", "loc", "org", "timezone"]

for field in fields:
    table.add_row(field.capitalize(), str(data.get(field, "N/A")))

c.print("[bold green]🛰️  Establishing orbital link...[/bold green]")

# 2. Run the animation (subprocess takes a clean list, no Rich tags here)
try:
    subprocess.run(["curl", "-s", "ascii.live/earth"], timeout=3)
except subprocess.TimeoutExpired:
    # This stops the infinite loop after 3 seconds
    c.clear()
    c.print("[bold cyan]✅ Link established. Fetching IP data...[/bold cyan]")

c.print(Panel(table, expand=False, border_style="green"))


                                                   
