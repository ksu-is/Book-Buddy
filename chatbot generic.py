import random

def get_response(user_input):
    """
    Returns a chatbot response based on the user's input.
    Checks for certain keywords and provides tailored reading advice.
    """
    text = user_input.lower()
    
    if "phonics" in text:
        return ("Phonics is a great way to help children sound out words. "
                "Start with simple words and focus on letter-sound associations.")
    elif "comprehension" in text:
        return ("Improving comprehension can be done by asking questions about the text "
                "and discussing the story together after reading.")
    elif "practice" in text:
        return ("Regular practice is key! Consider setting aside time each day for reading, "
                "and discuss the story as you go along.")
    elif "struggle" in text or "difficult" in text:
        return ("It sounds like you’re facing some challenges. Could you tell me more about what "
                "part of reading feels most difficult?")
    elif "tips" in text:
        return ("One helpful tip is to read aloud. This can boost both pronunciation and comprehension. "
                "Another idea is to use picture books to make reading fun!")
    elif "book" in text:
        return ("Choosing age-appropriate books is very important. Picture books and simple stories "
                "can be very effective for early reading development.")
    else:
        # Provide a generic response if no keyword is detected.
        generic_responses = [
            "That's interesting. Could you tell me a bit more?",
            "I see. What do you think is the most challenging part of reading right now?",
            "Let's explore that further. What would you like to work on?"
        ]
        return random.choice(generic_responses)

def save_conversation(user_text, bot_text, filename="conversation_log.txt"):
    """
    Appends the conversation (both user input and chatbot response) to a log file.
    """
    with open(filename, "a") as file:
        file.write("User: " + user_text + "\n")
        file.write("Bot: " + bot_text + "\n")
        file.write("-" * 40 + "\n")

def chat():
    """
    Main function to start the chatbot conversation.
    """
    print("Hello, I'm your Reading Coach Bot.")
    print("I'm here to help you with tips and guidance to support your child's reading journey.")
    print("Type 'exit' or 'quit' anytime to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! Happy reading!")
            break
        
        bot_response = get_response(user_input)
        print("Bot:", bot_response)
        save_conversation(user_input, bot_response)

if __name__ == "__main__":
    chat()
