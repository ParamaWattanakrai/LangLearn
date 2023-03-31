import spacy

nlp = spacy.load("zh_core_web_sm")
doc = nlp("我喜欢吃中餐 Hello")

i = 0
for token in doc:
    print(i)
    print(token, nlp(token).lang)
    i += 1