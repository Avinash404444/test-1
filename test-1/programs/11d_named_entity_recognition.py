# Install: pip install spacy
# Then run: python -m spacy download en_core_web_sm
import spacy

nlp = spacy.load("en_core_web_sm")
text = """Dr. Subashini works at SRM Institute of Science and Technology
in Tiruchirappalli. She organized an AI workshop on 15 September 2026."""
doc = nlp(text)
print("Named Entities:")
for entity in doc.ents:
    print(entity.text, "->", entity.label_)
