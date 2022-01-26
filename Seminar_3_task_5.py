# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]

# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(rep, arguments):

    """
    Function
    """
    get_lists = []
    for i in range(rep):
        a, b, c = choice(nouns), choice(adverbs), choice(adjectives)
        get_lists.append(f'{a} {b} {c}')
        if arguments is False:
            nouns.remove(a)
            adverbs.remove(b)
            adjectives.remove(c)
    print(get_lists)


get_jokes(rep=int(input("Введите количество шуток: ")), arguments=False)

