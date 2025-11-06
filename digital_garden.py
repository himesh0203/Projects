To Run

Save as digital_garden.py

Run it with:

python digital_garden.py







# digital_garden.py
# A living ASCII art garden that grows differently based on your mood or message.

import random
import time
import json
from pathlib import Path

GARDEN_FILE = Path("garden.json")

# Different plant growth styles
PLANT_PARTS = {
    "happy": ["🌻", "🌼", "🌞", "🍀", "🌸"],
    "sad": ["🥀", "🌫️", "🍂", "🌧️"],
    "angry": ["🌶️", "🔥", "🌵"],
    "calm": ["🌿", "🍃", "🌲", "🍀"],
    "dreamy": ["🌙", "✨", "🪷", "🌸"],
    "chaotic": ["💥", "🌪️", "🌾", "⚡"],
}

def detect_mood(text):
    """A simple mood detector using keywords."""
    text = text.lower()
    if any(word in text for word in ["happy", "joy", "great", "excited", "love"]):
        return "happy"
    elif any(word in text for word in ["sad", "lonely", "blue", "tired", "down"]):
        return "sad"
    elif any(word in text for word in ["angry", "mad", "furious", "rage"]):
        return "angry"
    elif any(word in text for word in ["peace", "calm", "relaxed", "chill"]):
        return "calm"
    elif any(word in text for word in ["dream", "wonder", "mystic", "sleepy"]):
        return "dreamy"
    else:
        return "chaotic"

def load_garden():
    """Load existing garden or start a new one."""
    if GARDEN_FILE.exists():
        return json.loads(GARDEN_FILE.read_text())
    return {"plants": []}

def save_garden(garden):
    """Save garden state."""
    GARDEN_FILE.write_text(json.dumps(garden, indent=2))

def grow_plant(mood):
    """Generate a small ASCII 'plant' based on mood."""
    parts = PLANT_PARTS.get(mood, PLANT_PARTS["chaotic"])
    height = random.randint(3, 7)
    plant = ""
    for i in range(height):
        plant += " " * random.randint(0, 4)
        plant += random.choice(parts) + "\n"
    plant += " " * random.randint(1, 3) + "🪴"
    return plant

def animate_growth(plant):
    """Animate the plant 'growing' on screen."""
    lines = plant.split("\n")
    for line in lines:
        print(line)
        time.sleep(0.3)

def main():
    print("🌱 Welcome to The Digital Garden 🌸")
    print("Each mood you share will grow a new plant.\n")

    garden = load_garden()

    mood_input = input("Describe your current mood or feeling:\n> ")
    mood = detect_mood(mood_input)

    print(f"\nDetected mood: {mood.upper()} — planting your seed... 🌱\n")
    plant = grow_plant(mood)
    animate_growth(plant)

    # Save it to the garden
    garden["plants"].append({"mood": mood, "art": plant})
    save_garden(garden)

    print("\n🌿 Your digital garden now has:")
    print(f"   {len(garden['plants'])} plants growing strong 🌸")
    print("\nWould you like to see your full garden? (y/n)")
    if input("> ").lower().startswith("y"):
        print("\n🌼 Your Garden 🌼")
        for i, p in enumerate(garden["plants"], start=1):
            print(f"\n#{i} ({p['mood']})")
            print(p["art"])
    print("\n🌎 See you next time — your garden will keep growing!\n")

if __name__ == "__main__":
    main()
