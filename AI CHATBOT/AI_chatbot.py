import nltk
from nltk.chat.util import Chat, reflections
import webbrowser



# Define patterns and responses for the chatbot
pairs = [
    ['hi', ['Hello!', 'Hi there!', 'How can I help you?']],
    ['what is your name', ['My name is Chatbot.', 'I am Chatbot.']],
    ['how are you', ['I am doing well, thank you.', 'I am fine, thanks for asking.']],
    ['bye', ['Goodbye!', 'Bye!', 'Have a nice day!']],
    ['tp stairs',['Tp stairs is the stairs for techpark building']],
    ['What is java ?',['Related to SRM College it is basically a cafeteria','If you want something else please mention once again']],
    ['Clock Tower',['The clock building(artifact) made up at the junction,which is infront of JAVA Cafeteria']],
    ['Where is UB building',['The most satisfying structure of art is you UB buidling which is painted in white colour.']],
    ['where is kalpana Chawla?',['Here is you link for the map of kalapna chawla:'
                                 'https://www.google.com/maps/place/Kalpana+Chawla+Hostel']],


    ['default', ['I am not sure what you are asking. Please try again.']]
]

# Create a chatbot using the defined patterns and responses
chatbot = Chat(pairs, reflections)

# Start a conversation with the chatbot
print("Hi, I'm SRM Chatbot. How can I help you today?")
while True:
    try:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print(response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

