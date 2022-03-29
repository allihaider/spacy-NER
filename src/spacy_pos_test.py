import spacy
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")

words  = ["My", "name", "is", "Ali", "and", "I", "like", "to", "play", "video", "games", "!"]
spaces = [True, True, True, True, True, True, True, True, True, True, False, False]

# POS should be a valid Universal Dependencies Tag
pos = ["NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN"]

deps = ["punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct"]

doc = Doc(nlp.vocab, words=words, spaces=spaces, pos=pos, deps=deps)

print(doc)

for token in doc:
	print(token.dep)
