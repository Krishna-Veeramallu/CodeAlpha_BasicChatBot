class ChatAssistant:
  """A simple chat assistant to answer basic questions and engage in small talk."""

  def __init__(self):
    """Initializes the chat assistant with predefined responses."""
    self.chat_data = {
      "hi": ["Hello, How can I assist you today?", "Hi there! What can I do for you?"],
      "how are you": ["I'm doing well, thank you for asking!"],
      "tell me about you": ["I'm a helpful chat assistant designed to answer your questions."],
      "help": ["Sure, I'm happy to help with anything I can."],
      "python_info": ["Python is a powerful and versatile programming language. It's known for its readability and ease of use.It's widely used for web development, data science, machine learning, and more!"],
      "thanks": ["You're welcome! Is there anything else I can do for you?"],
      "goodbye": ["Bye! Have a great day. See you later."],
      "weather": ["I don't have weather information at this moment, but I can search the web if you'd like."],
      "time": ["Unfortunately, I can't access the current time directly, but you can check your device's clock."],
      "day": ["Today is Monday, May 27th, 2024."],  # Adjust based on actual date
      "music": ["Can't recommend music directly, but I can search the web for you!"],
      "movies": ["Finding great movies is tough! Can I help you search the web for recommendations?"],
      "news":  ["Looking for news updates? I can search the web for you."],
      "fun_fact": ["Did you know the population of Earth is estimated to be over 8 billion people!"],
      "joke": ["Why did the scarecrow win an award? Because he was outstanding in his field! "]
    }

  def get_response(self, message):
    """Retrieves a response based on the user's message."""
    message = message.lower()
    for key in self.chat_data:
      if key in message:
        return self.chat_data[key]
    return "I apologize, I don't quite understand what you mean."

def chat_session():
  """Initiates and manages a chat session with the assistant."""
  assistant = ChatAssistant()
  print("\nWelcome to the Chat Assistant!")
  while True:
    user_message = input("You: ")
    response = assistant.get_response(user_message)
    if isinstance(response, list):
      print("Assistant:", response[0])  # Print only the first response for now
    else:
      print("Assistant:", response)
    if user_message.lower() == "goodbye":
      break

# Start the chat session
chat_session()
