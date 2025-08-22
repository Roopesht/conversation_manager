from utils import add_conversation
from utils import load_conversation, save_conversation, add_conversation
from openai_util import get_next_message
from perplexity import get_response
selected_person = ""

def show_menu():
    print("Main menu:")
    print("1. Select people")
    print ("2. Show conversation:")
    print ("3. Add conversation:")
    print ("4. What should be the response")

def show_people(data):
    global selected_person
    print("People:")

    # Show the list of people
    for i, person in enumerate(data["contacts"]):
        print(f"{i+1}. {person}")

    # Ask the user to select the person by typing the name
    name = input ("select the person by entering the name: ")
    if name in data['conversations']:
        selected_person = name
    else:
        print ("you entered wrong name")

def show_conversation(data):
    global selected_person
    print("Conversation:")
    node =  data["conversations"][selected_person]
    for conversation in node:
        print (conversation)
        #print(f" {conversation['text']} ({conversation['sender']})")

def add_conversation_method(data):
    global selected_person
    print("Add conversation:")
    text = input("Enter the text: ")
    sender = input("Enter the sender: ")
    datetime = "now"
    add_conversation(data, selected_person, text, sender, datetime)
    save_conversation(data, "data.json")

def get_response (node):
    message = get_next_message(node)
    conv = '\n'.join ([ f"{d['sender']} says `{d['text']}`"  for d in node ])
    #print (conv)
    system_msg = 'Your name is Roopesh, You are the owner of "Ojasa Mirai" a online Technical Training school. You need to respond to users in 1 short line.'
    user_msg = f'below is the conversation so far, please suggest the next dialogue from "Roopesh"\n conversation: {conv}'
    #print ("System msg: ", system_msg)
    #print ("user msg:  ", user_msg)
    resp = get_response(system_msg,user_msg)
    print ("\n\n", resp)




[{'datetime': '2025-08-01 10:00:00', 'sender': 'NTR', 'text': 'Hi Roopesh, I want to join your GenAI course'}, 
{'text': 'That is agreat choice.', 'sender': 'me', 'datetime': 'now'}]

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
            get_response(selected_person_node)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()