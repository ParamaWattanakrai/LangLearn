import spacy

nlp = spacy.load("de_dep_news_trf")
doc = nlp("%")
for token in doc:
    print(token)
    print(token.pos_)
    print(token.morph.get("Gender"))
    print(token.morph)
    print(token.lemma_)