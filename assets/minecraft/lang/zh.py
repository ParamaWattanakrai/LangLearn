import os
import json
import pinyin as py

C_PATH = os.path.dirname(__file__)
F_PATH = os.path.join(C_PATH, 'zh_cn_ori.json')

add_pinyin = lambda text: f'{text} ({py.get(text)})' if text != py.get(text) else text


with open(F_PATH, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())

i = 0

for value in data.values():
    converted = add_pinyin(value)
    data[key_list[i]] = converted
    print(data[key_list[i]])
    i += 1

with open('zh_cn.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)