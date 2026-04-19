import argparse
import sys
from generator import generate_horoscope, ZODIACS
from renderer import render_horoscope
from rich.console import Console

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Generate a hilarious ASCII horoscope.")
    parser.add_argument(
        "sign", 
        type=str, 
        nargs="?", 
        help="Your zodiac sign (e.g., aries, taurus, gemini...)"
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save the horoscope to a text file."
    )
    
    args = parser.parse_args()
    
    sign = args.sign
    if not sign:
        sign = console.input("[bold cyan]What is your zodiac sign? [/bold cyan]").strip().lower()
        
    sign = sign.lower()
    if sign not in ZODIACS:
        console.print(f"[bold red]Error:[/] '{sign}' is not a valid zodiac sign.")
        console.print(f"Valid signs: {', '.join(ZODIACS)}")
        sys.exit(1)
        
    # Generate data
    data = generate_horoscope(sign)
    
    # Render UI
    render_horoscope(data, save_to_file=args.save)

if __name__ == "__main__":
    main()
