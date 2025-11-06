# screen_time_philosopher.py
# A fun and original Python script that reflects on your screen time with humor and wisdom.

import random
import time

# Philosophical quotes for different moods
quotes = {
    "short": [
        "A moment well spent is a seed of eternity.",
        "Even a brief glance at the screen can shape your destiny.",
        "Time whispers: use me well.",
    ],
    "medium": [
        "Screens are mirrors; what do you see in yours?",
        "In the glow of pixels, remember: reality awaits beyond.",
        "Balance is not in quitting screens, but in mastering their pull.",
    ],
    "long": [
        "You’ve stared into the digital abyss, and it now stares back at you.",
        "In a world of endless scrolling, the true act of rebellion is to stop.",
        "Screens can’t blink — but maybe you should.",
    ],
}

def reflect_screen_time(seconds):
    """Return a philosophical quote based on screen time duration."""
    if seconds < 60:
        return random.choice(quotes["short"])
    elif seconds < 300:
        return random.choice(quotes["medium"])
    else:
        return random.choice(quotes["long"])

def simulate_screen_time():
    """Simulate user screen time tracking."""
    print("🖥️ Welcome to the Screen Time Philosopher 🧘‍♀️")
    print("Tracking your 'digital presence'... Press Ctrl+C to stop.\n")

    start = time.time()
    try:
        while True:
            elapsed = int(time.time() - start)
            mins, secs = divmod(elapsed, 60)
            print(f"\r⏳ Screen time: {mins}m {secs}s", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nSession ended.")
        print(f"Total screen time: {elapsed} seconds.\n")
        print("Philosopher says:")
        print(f"💬 {reflect_screen_time(elapsed)}")

if __name__ == "__main__":
    simulate_screen_time()
