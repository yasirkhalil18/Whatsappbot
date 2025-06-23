import json, re

# Load note links
with open("notes_data.json") as f:
    NOTES_DB = json.load(f)

SUBJECTS = {
    "math": "mathematics", "mathematics": "mathematics", "maths": "mathematics",
    "bio": "biology", "biology": "biology",
    "eng": "english", "english": "english",
    "phy": "physics", "physics": "physics",
    "chem": "chemistry", "chemistry": "chemistry",
    "isl": "islamiat", "islamiyat": "islamiat",
    "pak": "pak studies", "pak studies": "pak studies",
    "urdu": "urdu", "computer": "computer science", "cs": "computer science"
}

CLASSES = {
    "1st year": "11", "class 11": "11", "first year": "11",
    "2nd year": "12", "class 12": "12", "second year": "12",
    "matric": "10", "class 10": "10", "class 9": "9", "9th": "9"
}

BOARDS = {
    "fbise": "fbise", "federal": "fbise",
    "punjab": "punjab", "bise lahore": "punjab",
    "sindh": "sindh", "karachi": "sindh",
    "kpk": "kpk", "balochistan": "balochistan",
    "ajk": "ajk", "azad kashmir": "ajk"
}

GREETINGS = ["hello", "hi", "aoa", "salam", "notes", "help", "start"]

def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def generate_reply(user_msg):
    text = normalize(user_msg)

    if any(word in text.split() for word in GREETINGS):
        return "➤ Welcome to AiNotes.pk 👋 — Send your class, subject, and board to get free notes."

    cls = next((v for k, v in CLASSES.items() if k in text), None)
    subj = next((v for k, v in SUBJECTS.items() if k in text), None)
    board = next((v for k, v in BOARDS.items() if k in text), None)

    if not all([cls, subj, board]):
        return "➤ Please send your class, subject, and board (e.g., '2nd year math Punjab board')."

    for note in NOTES_DB:
        if note["class"] == cls and note["subject"] == subj and note["board"] == board:
            return f"Here’s your note:\n➤ {note['url']}"

    return "➤ Sorry, I couldn’t find notes for that. Please try a different subject or board."
