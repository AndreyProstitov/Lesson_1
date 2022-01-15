for i in range(1 , 101):
    if i % 10 == 5 or i % 10 == 6 or i % 10 == 7 or i % 10 == 8 or i % 10 == 9 or i % 10 == 0 or i % 100 == 11\
            or i % 100 == 12 or i % 100 == 13 or i % 100 == 14:
        print(i, "процентов")
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(i, "процента")
    elif i % 10 == 1:
        print(i, "процент")