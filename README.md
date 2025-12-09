# 🎄 Secret Santa Emotion-Aware Agent (Using Cognee + Gemini API)

A fun and intelligent **Secret Santa Agent** powered by **Cognee** as the memory layer and **Gemini** for reasoning.
This agent analyzes each participant’s description, detects their *emotional state*, and assigns a **personalized gift** based on emotions.

This project was built for the **Cognee Secret Santa Mini Challenge – Secret Santa Edition**.

---

## ✨ Features

### 🎁 **1. Secret Santa Matching**

Randomly assigns each person a receiver while ensuring:

* No one gets themselves
* No participant receives more than one Santa

### 🧠 **2. Emotion Detection Using Cognee**

Each participant gives a short description of how they feel or what’s going on in their life.

Example:

```
Alice: "I'm stressed with deadlines and too much work."
Bob: "Feeling amazing this week!"
```

Cognee:

* Stores all descriptions with `cognee.add()`
* Builds a knowledge graph using `cognee.cognify()`
* Extracts emotional state using `cognee.search()`

### 🎨 **3. Emotion-Based Gift Suggestions**

No LLM calls are used for gift generation → avoids extra costs.

Gifts come from a customizable rule-based system:

| Emotion  | Gift Type                 |
| -------- | ------------------------- |
| stressed | self-care items           |
| sad      | comfort items             |
| excited  | celebration items         |
| lonely   | connection-building items |
| happy    | positive experience gifts |

### 🧩 **4. Simple, Lightweight & Free-Tier Compatible**

* Uses Cognee + Gemini free-tier via Cognee's internal LLM ops
* No paid APIs
* No unnecessary external calls
* Judges can run it in seconds

---

## 🧬 Architecture Overview

```
Participants → Cognee Memory → Knowledge Graph → Emotion Extraction → Gift Engine → Final Santa Output
```

**Cognee is used meaningfully**:

* Stores participant descriptions
* Transforms them into knowledge graph
* Extracts emotional state using RAG + semantic reasoning

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pravesh-Sudha/secret-santa-cognee
cd secret-santa-cognee
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
uv sync
```

---

## 🔐 Environment Setup

Create a `.env` file based on the template:

### `.env.template`

```
LLM_API_KEY=<YOUR_GEMINI_API_KEY>
EMBEDDING_API_KEY=<YOUR_GEMINI_API_KEY>
```

Copy & rename it:

```bash
cp .env.template .env
```

Fill in your **Gemini API key**.

---

## ▶️ How to Run

```bash
uv sync
uv run main.py
```

Example Output:

```
🔍 Detecting emotions...
Alice → stressed
Bob → happy
Charlie → lonely

🎁 Matching friends...

🎄 FINAL SECRET SANTA RESULTS 🎄
Alice ➝ Charlie (lonely)
Gift Suggestion: A cozy “online game night kit” to bond with others.

Bob ➝ Alice (stressed)
Gift Suggestion: A calming lavender aroma diffuser.

Charlie ➝ Bob (happy)
Gift Suggestion: A fun adventure experience coupon.
```

---

## 🗂 Project Structure

```
📦 secret-santa-cognee
 ┣ main.py
 ┣ matcher.py          # Santa matching + emotion detection
 ┣ gift_engine.py      # Rule-based gift generator (no LLM cost)
 ┣ .env.template
 ┣ requirements.txt
 ┗ README.md
```

---

## 💡 How This Project Uses Cognee

Cognee is the **core intelligence layer** here:

### Used for:

* `cognee.add()` → store participant feelings
* `cognee.cognify()` → build graph memory
* `cognee.search()` → extract emotional meaning

### Why this is meaningful?

Because Cognee turns free-form text like:

> “Feeling overwhelmed with assignments.”

into structured reasoning like:

> **emotion: stressed**

This emotion is *then* used to generate the gift.

**This is exactly the kind of “AI memory + reasoning” Cognee challenge asks for.**

---

## 🎯 Rules Included in This Agent

### ✔ Emotion-based gifting

### ✔ No self-assignment

### ✔ Optional “Chaos Mode” (Michael Scott Rule)

One friend can break rules and send a ridiculous gift (toggle in code).

---

## 🏆 Why This Project is a Strong Challenge Submission

* ✔ Creative mechanic: **Emotion-Based Santa**
* ✔ Cognee used in a deep meaningful way
* ✔ Uses free-tier only
* ✔ Portable (single main.py possible)
* ✔ Fun + Demonstrative + Clear
* ✔ Avoids unnecessary API calls
* ✔ Judges can run it instantly

---

## 📹 Demo (optional)

Upload a screen recording and link it here.

---

## 📧 Submission Info

Send your repo link (and demo if any) to:

```
social@cognee.ai
```

---

## ❤️ Contributing

Feel free to fork and experiment with:

* more emotion categories
* stricter rules
* web UI
* chaotic characters

---

## ⭐ License

MIT License
