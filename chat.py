print("===== WELCOME TO PYTHON CHATBOT =====")

print("Hello! I am your Python Chatbot.")

while True:
    user = input("\nYou: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "your name":
        print("Bot: I am Python Chatbot.")

    elif user == "help":
        print("Bot: How can I help you?")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")