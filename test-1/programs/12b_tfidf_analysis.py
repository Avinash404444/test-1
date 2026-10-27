# Install: pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Machine learning is a part of artificial intelligence",
    "Artificial intelligence uses machine learning",
    "Natural language processing is a part of artificial intelligence"
]
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(documents)
features = vectorizer.get_feature_names_out()
print("TF-IDF Values:\n")
for i, row in enumerate(matrix.toarray()):
    print("Document", i + 1)
    for word, value in zip(features, row):
        if value > 0:
            print(word, "->", round(value, 3))
    print()
