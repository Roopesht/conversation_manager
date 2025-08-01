
from utils import load_conversation, add_conversation
import json

data = load_conversation("data.json")


add_conversation(data, "NTR", "Please join, when you are starting?", "me", "now")


# save data to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

