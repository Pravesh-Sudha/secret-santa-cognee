import asyncio
import json
from cognee import SearchType
import cognee
from matcher import detect_emotions, match_friends
from gift_gen import generate_gift

async def main():

    # Reset Cognee internal state
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)

    # Load friends
    friends = json.load(open("data/friends.json"))

    print("📥 Adding profiles to Cognee...")
    for f in friends:
        await cognee.add(f"{f['name']}: {f['bio']}")

    print("🧠 Cognifying data...")
    await cognee.cognify()

    print("🔍 Detecting emotions...")
    emotions = {}
    for f in friends:
        emo = await detect_emotions(f["name"])
        emotions[f["name"]] = emo
        print(f" - {f['name']} → {emo}")

    # Attach emotion back to list
    for f in friends:
        f["emotion"] = emotions[f["name"]]

    print("\n🎁 Matching friends...")
    assignments = match_friends(friends)

    print("\n🎄 FINAL SECRET SANTA RESULTS 🎄\n")
    for giver, receiver in assignments.items():
        receiver_emo = emotions[receiver]
        gift = generate_gift(receiver, receiver_emo)

        print(f"{giver} ➝ {receiver} ({receiver_emo})")
        print(f"Gift Suggestion: {gift}\n")


if __name__ == "__main__":
    asyncio.run(main())