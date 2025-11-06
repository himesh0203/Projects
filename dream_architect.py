# dream_architect.py
# A creative Python script that builds surreal dream descriptions using procedural generation.

import random
import textwrap

# Dream components
settings = [
    "an infinite library of floating books",
    "a city built entirely of glass and moonlight",
    "a desert where every grain of sand whispers secrets",
    "an ocean suspended upside down in the sky",
    "a forest made of luminous circuits",
    "a labyrinth of living mirrors",
]

characters = [
    "a time-traveler who remembers the future",
    "a child made of starlight",
    "a talking fox wearing a crown of static",
    "an astronaut lost between dimensions",
    "a machine learning to dream",
    "a poet who can only speak in echoes",
]

emotions = [
    "nostalgic wonder",
    "quiet dread",
    "melancholic beauty",
    "restless curiosity",
    "calm transcendence",
    "chaotic joy",
]

artifacts = [
    "a pocket watch beating like a heart",
    "a key that unlocks forgotten memories",
    "a book that writes itself as you dream",
    "a mirror that shows who you could have been",
    "a melody trapped inside a crystal sphere",
]

twists = [
    "Time begins to flow backward.",
    "Gravity disappears, and thoughts become physical objects.",
    "You realize everyone else is a reflection of you.",
    "The dream starts dreaming you instead.",
    "Reality resets, but only you remember.",
    "You wake up inside someone else's dream.",
]

def generate_dream():
    """Generate a surreal dream description."""
    setting = random.choice(settings)
    character = random.choice(characters)
    emotion = random.choice(emotions)
    artifact = random.choice(artifacts)
    twist = random.choice(twists)

    dream = (
        f"In {setting}, you encounter {character}. "
        f"The air is thick with {emotion}. "
        f"They hand you {artifact}. "
        f"As you hold it, {twist}"
    )

    return textwrap.fill(dream, width=80)

if __name__ == "__main__":
    print("🌙 Welcome to the Dream Architect 💤\n")
    dream = generate_dream()
    print(dream)
    print("\n✨ End of dream ✨")
