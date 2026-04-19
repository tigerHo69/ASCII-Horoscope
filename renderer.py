from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

COLORS = {
    "aries": "red",
    "taurus": "green",
    "gemini": "yellow",
    "cancer": "cyan",
    "leo": "dark_orange",
    "virgo": "green",
    "libra": "magenta",
    "scorpio": "dark_red",
    "sagittarius": "purple",
    "capricorn": "white",
    "aquarius": "blue",
    "pisces": "blue"
}

def render_horoscope(horoscope_data: dict, save_to_file: bool = False):
    sign = horoscope_data["sign"].lower()
    color = COLORS.get(sign, "magenta")
    
    # Generate ASCII Art for the sign
    f = Figlet(font='slant')
    ascii_art = f.renderText(horoscope_data['sign'])
    
    # Assemble the content
    content = Text()
    content.append(ascii_art, style=f"bold {color}")
    content.append("\n" + "· "*20 + "\n\n", style="dim")
    
    content.append(f"{horoscope_data['text']}\n\n", style="bold white")
    
    details = Text()
    details.append(f"🍀 Lucky Object: ", style="bold green")
    details.append(f"{horoscope_data['lucky_object']}\n", style="white")
    details.append(f"🔢 Lucky Number: ", style="bold cyan")
    details.append(f"{horoscope_data['lucky_number']}\n", style="white")
    details.append(f"🎨 Lucky Color:  ", style="bold magenta")
    details.append(f"{horoscope_data['color']}", style="white")
    
    content.append(details)
    
    panel = Panel(
        Align.center(content),
        title="[bold yellow]✨ DAILY HOROSCOPE ✨[/bold yellow]",
        border_style=color,
        padding=(1, 4),
        expand=False
    )
    
    console.print("\n")
    console.print(Align.center(panel))
    console.print("\n")
    
    if save_to_file:
        with open(f"horoscope_{sign}.txt", "w") as file:
            c = Console(file=file, force_terminal=False)
            c.print("\n")
            # We must print the ascii art without rich formatting if we want plain text
            file.write(ascii_art)
            file.write("\n" + "· "*20 + "\n\n")
            file.write(f"{horoscope_data['text']}\n\n")
            file.write(f"Lucky Object: {horoscope_data['lucky_object']}\n")
            file.write(f"Lucky Number: {horoscope_data['lucky_number']}\n")
            file.write(f"Lucky Color:  {horoscope_data['color']}\n\n")
        console.print(f"[dim]Horoscope saved to horoscope_{sign}.txt for easy sharing![/dim]\n")
