import os
import json

import spacy

nlp = spacy.load("de_dep_news_trf")

C_PATH = os.path.dirname(__file__)
F_PATH = os.path.join(C_PATH, 'de_processed.json')

with open(F_PATH, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())

i = 0
for value in data.values():
    value = value.replace('\u00A75', '\u00A7a')
    data[key_list[i]] = value
    i += 1

with open('replaced.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)