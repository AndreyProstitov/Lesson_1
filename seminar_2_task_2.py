#2. Дан список:
#['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

#Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
#['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

#Сформировать из обработанного списка строку:
#в "05" часов "17" минут температура воздуха была "+05" градусов

#Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?


weather_forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
#print(weather_forecast)
# index = weather_forecast.index('5')
# weather_forecast[index] = '"05"'
# index = weather_forecast.index('+5')
# weather_forecast[index] = '"+05"'
# index = weather_forecast.index('17')
# weather_forecast[index] = '"17"'
for ind, val in enumerate(weather_forecast):
    sign_1 = "'"
    sign_2 = ""
    if val.isdigit():
        weather_forecast[ind] = f"{sign_1}{int(val):02}{sign_1}"
    if val.count('+'):
        val = val.replace("+", "")
        sign_2 = "+"
        weather_forecast[ind] = f"{sign_1}{sign_2}{int(val):02}{sign_1}"
    elif val.count('-'):
        val = val.replace("-", "")
        sign_2 = "-"
        weather_forecast[ind] = f"{sign_1}{sign_2}{int(val):02}{sign_1}"

print(" ".join(weather_forecast))




#print(weather_forecast)
#print(" ".join(weather_forecast))
