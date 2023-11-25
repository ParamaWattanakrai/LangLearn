import os
import json

import spacy

C_PATH = os.path.dirname(__file__)
F_PATH = os.path.join(C_PATH, 'de_template.json')

with open(F_PATH, 'r', encoding='utf8') as f:
    d = f.read()
    data = json.loads(d)

key_list = list(data.keys())