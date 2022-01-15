duration = int(input("Введите количество секунд: "))

day = duration // 86400 # 1 день = 86400 сек
duration %= 86400
hour = duration // 3600 # 1 час = 3600 сек
duration %= 3600
minute = duration // 60 # 1 мин = 60 сек
duration %= 60
sec = duration
print (f"{day} дн, {hour} ч, {minute} мин, {sec} сек")