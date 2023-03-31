import os

C_PATH = os.path.dirname(__file__)
F_PATH = os.path.join(C_PATH, 'ja_y.json')

import json

import pykakasi
kks = pykakasi.kakasi()

def to_katakana(text):
    result = kks.convert(text)
    katakana = ''
    for item in result:
        katakana = katakana + item['kana']
    return katakana

file_path = 'C:/Users/PN_Pengy/AppData/Roaming/.minecraft/resourcepacks/LangLearn/assets/minecraft/lang/ja_y.json'

with open(F_PATH, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())

i = 0
for value in data.values():
    converted = (value + ' (' + to_katakana(value) + ')')
    data[key_list[i]] = converted
    print(data[key_list[i]])
    i = i+1

with open('ja_x.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)