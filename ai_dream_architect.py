pip install openai

export OPENAI_API_KEY="your-key-here"

python ai_dream_architect.py



# ai_dream_architect.py
# A poetic, GPT-powered dream generator that transforms surreal ideas into stories.

import os
import random
import textwrap
from openai import OpenAI

# Initialize GPT client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY") or "your-api-key-here")

# Dream seeds
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


def generate_dream_seed():
    """Create a short surreal dream concept."""
    setting = random.choice(settings)
    character = random.choice(characters)
    emotion = random.choice(emotions)
    artifact = random.choice(artifacts)
    twist = random.choice(twists)

    return (
        f"In {setting}, you encounter {character}. "
        f"The air is thick with {emotion}. "
        f"They hand you {artifact}. "
        f"As you hold it, {twist}"
    )


def expand_with_ai(dream_seed):
    """Use GPT to expand the dream into a poetic short story."""
    prompt = (
        "You are a surreal dream narrator. Expand the following dream seed "
        "into a short poetic story (about 3–5 paragraphs). "
        "Write vividly, emotionally, and with imaginative depth.\n\n"
        f"Dream seed: {dream_seed}\n\nDream story:"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-4o if available
        messages=[
            {"role": "system", "content": "You write poetic, dreamlike short stories."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.9,
    )

    story = response.choices[0].message.content.strip()
    return story


if __name__ == "__main__":
    print("🌙 Welcome to the AI Dream Architect 💤\n")
    seed = generate_dream_seed()
    print("💭 Dream seed:")
    print(textwrap.fill(seed, width=80))
    print("\n✨ Building dream...\n")

    story = expand_with_ai(seed)
    print(story)
    print("\n🌌 End of dream 🌌")
