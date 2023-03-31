import time

import json
from googletrans import Translator
translator = Translator(service_urls=['translate.google.com'])

file_path = 'C:/Users/PN_Pengy/AppData/Roaming/.minecraft/resourcepacks/LangLearn/assets/minecraft/lang/de_y.json'

with open(file_path, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())

i = 0
for value in data.values():
    try:
        translation = translator.translate(value, src='de', dest='en')
        while translation.text is None:
            continue
        print(translation)
        data[key_list[i]] = translation.text
        print(data[key_list[i]])
        i = i+1
    except Exception as e:
        print("WHY ARE YOU TORTURING ME, WHERE ARE MY KIDS")
        time.sleep(1)
    if i is 11:
        break

print(data)

with open('example_en.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
