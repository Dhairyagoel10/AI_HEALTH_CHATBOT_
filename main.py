from chatbot_logic import create_chatbot

# Initialize the chatbot
chatbot = create_chatbot()

print("Health Chatbot is ready to answer your queries!")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
