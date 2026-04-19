import random

ZODIACS = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo", 
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]

OPENINGS = [
    "The stars indicate that",
    "Mercury is in retrograde, meaning",
    "Your ruling planet is aligning, so",
    "The cosmic energy is chaotic today, meaning",
    "According to the ancient scrolls,",
    "A disruption in the space-time continuum reveals that"
]

PREDICTIONS = [
    "you shouldn't trust anyone wearing a hat today.",
    "your code will inevitably refuse to compile.",
    "you will find the answer you seek in a discarded fast-food wrapper.",
    "an unexpected bird will offer you sage financial advice.",
    "you should avoid maintaining eye contact with your houseplants.",
    "your Wi-Fi will demand a blood sacrifice.",
    "a stranger will compliment your posture, but they are lying.",
    "you will accidentally deploy straight to production. Good luck.",
    "all your passwords will suddenly feel inadequate.",
    "you must walk backwards to avoid a minor inconvenience.",
    "a minor typo will radically change the trajectory of your life.",
    "the ghosts in your codebase are plotting against you."
]

LUCKY_OBJECTS = [
    "A used napkin", "A single left shoe", "A confused pigeon", 
    "A floppy disk", "A mechanical keyboard", "A half-eaten sandwich",
    "Your rubber duck", "A mysterious loose screw", "A slightly bent spoon",
    "A seemingly infinite loop"
]

def generate_horoscope(sign: str) -> dict:
    return {
        "sign": sign.capitalize(),
        "text": f"{random.choice(OPENINGS)} {random.choice(PREDICTIONS)}",
        "lucky_object": random.choice(LUCKY_OBJECTS),
        "lucky_number": random.randint(1, 99),
        "color": random.choice(["Neon Pink", "Cyber Green", "Void Black", "Cosmic Purple", "Syntax Error Red", "Warning Yellow"])
    }
