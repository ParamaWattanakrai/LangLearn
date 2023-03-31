import spacy

#nlp = spacy.load("de_core_news_sm")
#nlp = spacy.load("de_core_news_md")
#nlp = spacy.load("de_core_news_lg")
nlp = spacy.load("de_dep_news_trf")

text = 'Pfeil des Schadens'

doc = nlp(text)

for token in doc:
    print(token.text, token.pos_, token.dep_, token.morph)

