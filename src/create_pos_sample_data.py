import spacy
from spacy.tokens import Doc
from spacy.tokens import DocBin

nlp = spacy.load("en_core_web_sm")

words  = ["My", "name", "is", "Ali", "and", "I", "like", "to", "play", "video", "games", "!"]
spaces = [True, True, True, True, True, True, True, True, True, True, False, False]
tags = ["NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "RP", "RP", "RP"]

doc = Doc(nlp.vocab, words=words, spaces=spaces, tags=tags)
print(f"Created doc: {doc}")

print("Doc tags:")
for token in doc:
	print(token.tag_, end=", ")

db = DocBin()
db.add(doc)
db.to_disk("../data/pos-data/train-pos.spacy")

# POS should be a valid Universal Dependencies Tag
# pos = ["NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN", "NOUN"]
# deps = ["punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct", "punct"]
