cube_list = []

for i in range(1, 1001, 2):
    cube_list.append(i**3) # Создание списка и возведение числа в куб
sum_n = 0
for n in cube_list:
    s_m = 0
    m = n
    while m:
        s_m += m % 10   # Сумма цифр числа
        m = m // 10     # Убираем остаток
    if s_m % 7 == 0:
        sum_n += n      # Сумма нужных чисел из списка
print(sum_n)

sum_n = 0               # создание нового списка--> cube_list.append(i**3 + 17)
for n in cube_list:     # Выполняем сразу задание со зведочкой без создания нового списка.
    s_m = 0
    n += 17             # Увеличиваем число списка на 17
    m = n
    while m:
        s_m += m % 10   # Сумма цифр числа
        m = m // 10     # Убираем остаток

    if s_m % 7 == 0:
        sum_n += n      # Сумма нужных чисел из списка
print(sum_n)
