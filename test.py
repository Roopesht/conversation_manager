
from utils import load_conversation, add_conversation, save_conversation
import json

data = load_conversation("data.json")

add_conversation(data, "NTR", "Please join, when you are starting?", "me", "now")

save_conversation(data, "data.json")

