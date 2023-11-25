import os
import json

import spacy

nlp = spacy.load("de_dep_news_trf")

C_PATH = os.path.dirname(__file__)
F_PATH = os.path.join(C_PATH, 'de_template.json')

with open(F_PATH, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())

i = 0
for value in data.values():
    doc = nlp(value)
    converted_text = ''
    for token in doc:
        coded_noun = token.text
        if token.pos_ == "NOUN" and token.morph.get("Gender"):
            gender = token.morph.get("Gender")[0]
            if gender == 'Masc':
                prefix = '\u00A79'
            if gender == 'Fem':
                prefix = '\u00A7c'
            if gender == 'Neut':
                prefix = '\u00A75'
            coded_noun = prefix + token.text + '\u00A7r'
        if token.pos_ == "PUNCT":
            converted_text += coded_noun
        else:
            converted_text += ' ' + coded_noun
    converted_text = converted_text[1:]
    converted_text = converted_text.replace('‚ ', ' ‚')
    converted_text = converted_text.replace('„ ', ' „')
    data[key_list[i]] = converted_text
    if i % 43 == 0:
        print(f'{i}/{len(key_list)}: {converted_text}')
    i += 1

with open('de_processed.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)