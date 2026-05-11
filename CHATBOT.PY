def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit the conversation.")
    
    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("You: ").lower().strip()
        
        # Logic using if-elif-else
        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi!")
            
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
            
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit the loop
            
        else:
            print("Chatbot: I'm sorry, I don't understand that. Try 'hello' or 'how are you'.")

# Start the chatbot
if __name__ == "__main__":
    chatbot()