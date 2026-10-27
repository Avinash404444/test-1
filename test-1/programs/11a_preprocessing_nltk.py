# Install: pip install nltk
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

text = "NLTK and spaCy are great libraries for Natural Language Processing!"
tokens = word_tokenize(text)
print("Tokens:")
print(tokens)
tokens = [word.lower() for word in tokens]
stop_words = set(stopwords.words("english"))
filtered = [word for word in tokens if word.isalpha() and word not in stop_words]
print("\nAfter Stop Word Removal:")
print(filtered)
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered]
print("\nAfter Preprocessing with NLTK:")
print(lemmatized)
