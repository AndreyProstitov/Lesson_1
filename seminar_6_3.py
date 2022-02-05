from itertools import zip_longest
import json


def user_hob(text):
    with open(text, "r", encoding='utf-8') as f:
        for i in f:
            yield i.replace(',', ' ').strip()


with open('hobby_3.json', 'w', encoding='utf-8') as file:
    rerere = {}
    for key, val in zip_longest(user_hob('users.csv'), user_hob('hobby.csv')):
        rerere.setdefault(key, val)
        if key is None:
            exit(1)
    json.dump(rerere, file, ensure_ascii=False, indent=4)
