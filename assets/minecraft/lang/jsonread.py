import os

C_PATH = os.path.dirname(__file__)
F_PATH = os.path.join(C_PATH, 'ja_y.json')

import json

import time

from googletrans import Translator
translator = Translator(service_urls=['translate.google.com'])

with open(F_PATH, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())

def detect_gender(wort):
    
    word = translator.translate(wort, dest='en', src='de').text
    wordthe = 'the ' + word
    print(wordthe)

    translation = translator.translate(wordthe, dest='de', src='en').text
    print(translation)

    artikel = translation.split(" ")[0].lower()
    print(artikel)
    
    if artikel == 'der' or 'die' or 'das':
        return artikel
    else:
        return 'AttentionQUIRKYWORD'

i = 0
for wort in data.values():
    try:
        artikel = detect_gender(wort)
        print(artikel)
        data[key_list[i]] = artikel + " " + data[key_list[i]]
        print(data[key_list[i]])
        i = i+1
    except Exception as e:
        print("WHY ARE YOU TORTURING ME, WHERE ARE MY KIDS, PLEASE SPARE THEM!")
        time.sleep(1)
    if i is 11:
        break

print(data)

with open('example_en.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

import json

from googletrans import Translator
translator = Translator(service_urls=['translate.google.com'])
