import json
def save_conversation(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Load from JSON file
def load_conversation(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_conversation(data, contact, text, sender, datetime ):
    data.append({
        "contact": contact,
        "text": text,
        "sender": sender,
        "datetime": datetime
    })

