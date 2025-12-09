import random

def generate_gift(name, emotion):
    # Pre-defined gifts for each emotion
    gift_options = {
        "happy": [
            "A fun board game 🎲",
            "A personalised keychain 🔑",
            "A cute desk plant 🌱",
            "A box of chocolates 🍫",
            "A handwritten appreciation note ✍️"
        ],
        "stressed": [
            "A stress relief ball set 🧘‍♂️",
            "A scented candle 🕯️",
            "A self-care kit 🛁",
            "A warm cozy blanket 🧣",
            "A calming herbal tea pack 🍵"
        ],
        "lonely": [
            "A friendship bracelet 🤝",
            "A cute plush toy 🧸",
            "A small photo frame with your memories 🖼️",
            "A handwritten letter 💌",
            "A little snack hamper 🍪"
        ],
        "excited": [
            "A colourful notebook 📓",
            "A surprise mystery box 🎁",
            "A box of energy snacks ⚡",
            "A quirky desk toy 🧩",
            "A celebration cupcake 🧁"
        ],
        # fallback if emotion not found
        "neutral": [
            "A nice pen set 🖊️",
            "A chocolate bar 🍫",
            "A greeting card ✉️"
        ]
    }

    # Use neutral list if no emotion matches
    gifts = gift_options.get(emotion, gift_options["neutral"])

    return random.choice(gifts)
