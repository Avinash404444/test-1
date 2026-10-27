# Install: pip install spacy
# Then run: python -m spacy download en_core_web_sm
import spacy

nlp = spacy.load("en_core_web_sm")
text = "NLTK and spaCy are great libraries for Natural Language Processing!"
doc = nlp(text)
processed_words = [
    token.text.lower()
    for token in doc
    if not token.is_punct and not token.is_stop and token.is_alpha
]
print("Original Text:")
print(text)
print("\nAfter Preprocessing with spaCy:")
print(processed_words)
