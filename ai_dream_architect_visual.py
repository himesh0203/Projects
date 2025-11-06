pip install openai requests


export OPENAI_API_KEY="your-key-here"


python ai_dream_architect_visual.py






# ai_dream_architect_visual.py
# An AI-powered dream generator that creates both a poetic story and an AI image.

import os
import random
import textwrap
from openai import OpenAI
from pathlib import Path

# Initialize GPT + DALL·E client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY") or "your-api-key-here")

# Dream building blocks
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
    """Create a surreal dream concept."""
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
        "into a short poetic story (3–5 paragraphs). Be vivid, emotional, and otherworldly.\n\n"
        f"Dream seed: {dream_seed}\n\nDream story:"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4o" if you have it
        messages=[
            {"role": "system", "content": "You write poetic, dreamlike short stories."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.9,
    )

    return response.choices[0].message.content.strip()


def create_dream_image(prompt, save_path="dream_image.png"):
    """Use DALL·E to create an image that represents the dream."""
    print("\n🎨 Generating dream image...")

    image = client.images.generate(
        model="dall-e-3",
        prompt=f"Surreal digital art depicting: {prompt}. Dreamlike, cinematic lighting, ethereal, poetic atmosphere.",
        size="1024x1024",
    )

    image_url = image.data[0].url

    # Optionally download image
    import requests
    img_data = requests.get(image_url).content
    Path(save_path).write_bytes(img_data)

    print(f"🖼️ Dream image saved as {save_path}")
    print(f"🔗 Image URL: {image_url}")
    return save_path


if __name__ == "__main__":
    print("🌙 Welcome to the AI Dream Architect — Visual Edition 💫\n")
    seed = generate_dream_seed()
    print("💭 Dream seed:")
    print(textwrap.fill(seed, width=80))

    print("\n✨ Writing your dream...\n")
    story = expand_with_ai(seed)
    print(story)

    create_dream_image(seed)

    print("\n🌌 End of dream 🌌")
