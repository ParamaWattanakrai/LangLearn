import os
import json

import pykakasi
kks = pykakasi.kakasi()

C_PATH = os.path.dirname(__file__)
F_PATH = os.path.join(C_PATH, 'ja_y.json')

def detect_scripts(item):
    hiragana_range = range(0x3040, 0x30A0)
    katakana_range = range(0x30A0, 0x3100)
    kanji_range = range(0x4E00, 0x9FBF)
    if ord(item[0]) in hiragana_range:
        color = '\u00A7b'
    elif ord(item[0]) in katakana_range:
        color = '\u00A73'
    elif ord(item[0]) in kanji_range:
        color = '\u00A79'
    else:
        color = '\u00A7a'
    return color

def to_hiragana(text):
    result = kks.convert(text)
    orig_str = ''
    hiragana_str = ''
    if '%' in text or '$' in text:
        converted = text
    else:
        for item in result:
            color = detect_scripts(str(item['orig']))
            orig_str = orig_str + color + item['orig']
            hiragana_str = hiragana_str + color + item['hira']
        if '\u00A79' in orig_str:
            converted = orig_str + ' \u00A7r(' + hiragana_str + '\u00A7r)'
        else:
            converted = orig_str
    return converted

with open(F_PATH, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())

i = 0
for value in data.values():
    data[key_list[i]] = to_hiragana(value)
    i += 1

with open('ja_x.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)