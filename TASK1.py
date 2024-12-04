# Simple Rule-Based Chatbot

def chatbot():
    print("Hello! I'm a simple AI chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("MY AI CHAT: Goodbye! Have a great day!")
            break

        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("MY AI CHAT: Hi there! How can I assist you today?")

        # Asking about the chatbot
        elif "who are you" in user_input or "what is your name" in user_input:
            print("MY AI CHAT : I am a simple chatbot created to help you with basic tasks.")

        # Asking about the weather
        elif "weather" in user_input:
            print("MY AI CHAT: I'm not connected to the internet, but you can check your local weather app!")

        # Asking for the time
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"MY AI CHAT: The current time is {current_time}.")

        # Generic fallback
        else:
            print("MY AI CHAT: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
