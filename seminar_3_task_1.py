# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

# def num_translate(words):
#     print(translate.get(words))
#
# num_translate(input("Please, enter number: ").capitalize())

def num_translate_adv(words):
    if words.istitle():
        print(str(translate.get(words.lower())).capitalize())
    else:
        print(str(translate.get(words)))

num_translate_adv(input("Please, enter number: "))
