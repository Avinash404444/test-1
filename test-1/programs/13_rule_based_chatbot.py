# Install: pip install nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?"]],
    [r"what is your name?", ["I am a simple rule-based chatbot."]],
    [r"how are you?", ["I am fine. Thank you!"]],
    [r"what can you do?", ["I can answer simple questions using predefined rules."]],
    [r"bye|quit|exit", ["Goodbye! Have a nice day."]]
]
chatbot = Chat(pairs, reflections)
print("Chatbot: Hello! Type 'quit' to exit.")
chatbot.converse()
