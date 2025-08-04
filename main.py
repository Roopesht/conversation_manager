from utils import add_conversation
from utils import load_conversation, save_conversation, add_conversation
from openai_util import get_next_message
selected_person_node = None
def show_menu():
    global selected_person_node
    print("Main menu:")
    print("1. Select people")
    print ("2. Show conversation:")
    print ("3. Add conversation:")
    print ("4. What should be the response")

def show_people(data):
    global selected_person_node
    print("People:")
    for i, person in enumerate(data["contacts"]):
        print(f"{i+1}. {person}")
    name = input ("select the person by entering the name: ")
    if name in data['conversations']:
        selected_person_node = data['conversations'][name]
    else:
        print ("you entered wrong name")

def show_conversation(data):
    global selected_person_node
    print("Conversation:")
    for conversation in selected_person_node:
        print (conversation)
        #print(f" {conversation['text']} ({conversation['sender']})")

def add_conversation_method(data):
    global selected_person_node
    print("Add conversation:")
    text = input("Enter the text: ")
    sender = input("Enter the sender: ")
    datetime = "now"
    add_conversation(data, "NTR", text, sender, datetime)
    save_conversation(data, "data.json")

def get_response (node):
    message = get_next_message(node)
    add_conversation(data, "MTR", message, "me", "now")

def main ():
    data = load_conversation("data.json")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            show_people(data)
        elif choice == "2":
            show_conversation(data)
        elif choice == "3":
            add_conversation_method(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()