# Install: pip install nltk
import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger_eng")
from nltk.tokenize import word_tokenize

text = "The student is studying Artificial Intelligence."
tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
print("POS Tags:")
for word, tag in pos_tags:
    print(word, "->", tag)
