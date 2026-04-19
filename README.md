# ✨ ASCII Horoscope Generator ✨

A command-line tool that generates hilarious daily horoscopes with styled ASCII art in the terminal. No need for actual astrological alignment—it operates based on raw chaotic energy.

## Features
- **Absurd Predictions**: Generates unpredictable daily insights, along with lucky numbers and arbitrary "lucky objects".
- **Beautiful Terminal Output**: Powered by `rich` and `pyfiglet` for clean borders and colorful fonts.
- **Export to File**: Save your daily horoscope to a `.txt` file to easily share with friends!

## Installation

Ensure you have Python installed, then set up the environment:

```bash
# Clone the repository
git clone https://github.com/tigerHo69/ASCII-Horoscope.git
cd ASCII-Horoscope

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## How to Run

Pass your zodiac sign as an argument when running the script:

```bash
python main.py taurus
```

If you don't provide a sign, the program will gracefully ask for it!

### Exporting
To save the output as a clean `.txt` file without terminal styling, use the `--save` flag:

```bash
python main.py aries --save
```

## Example Output

```text
╭─────────────────────────── ✨ DAILY HOROSCOPE ✨ ────────────────────────────╮
│                                                                              │
│           ___         _                                                      │
│          /   |  _____(_)__  _____                                            │
│         / /| | / ___/ / _ \/ ___/                                            │
│        / ___ |/ /  / /  __(__  )                                             │
│       /_/  |_/_/  /_/\___/____/                                              │
│                                                                              │
│                                                                              │
│       · · · · · · · · · · · · · · · · · · · ·                                │
│                                                                              │
│       The stars indicate that you will find the answer you seek in a         │
│       discarded fast-food wrapper.                                           │
│                                                                              │
│       🍀 Lucky Object: A half-eaten sandwich                                 │
│       🔢 Lucky Number: 81                                                    │
│       🎨 Lucky Color:  Neon Pink                                             │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
```