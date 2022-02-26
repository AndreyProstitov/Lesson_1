class DigitList(Exception):
    def __init__(self, num):
        self.num = num


my_list = []
while True:
    number_to_list = input()
    try:
        if number_to_list == 'stop':
            break
        if not number_to_list.isdigit():
            raise DigitList('Некорректный ввод')
        number_to_list = int(number_to_list)
        my_list.append(number_to_list)

    except DigitList as error:
        print(error)

print(my_list)
