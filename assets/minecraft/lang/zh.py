import os
import json
import pinyin as py
import spacy

nlp = spacy.load("zh_core_web_sm")

C_PATH = os.path.dirname(__file__)
F_PATH = os.path.join(C_PATH, 'zh_y.json')

#add_pinyin = lambda text: f'{text} ({py.get(text)})' if text != py.get(text) else text

def convert(text):
    doc = nlp(text)
    pinyin_str = ''
    i = 0
    for token in doc:
        if i == 0:
            i += 1
            pinyin_str = pinyin_str + py.get(token.text)
        else:
            i += 1
            pinyin_str = pinyin_str + ' ' + py.get(token.text)
    return f'{text} ({pinyin_str})'

with open(F_PATH, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())

i = 0

for value in data.values():
    converted = convert(value)
    data[key_list[i]] = converted
    print(data[key_list[i]])
    i += 1

with open('zh_x.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)