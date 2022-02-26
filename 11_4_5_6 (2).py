class OrgTeh:
    model = ["LG", 'Samsung']
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.price = 3000
        self.order = []


    def realiz(self):
        while True:
            tovar = ''
            try:
                zapros = int(input('укажите необходимый тип: \n1 - принтер \n2 - сканер \n3 - ксерокс\n'))
                if zapros == 'q':
                    break
                if zapros == 1:
                    tovar = 'printer'
                    print(Warehouse.max_stock)
                elif zapros == 2:
                    tovar = 'scaner'
                    print(Warehouse.max_stock_scan)
                elif zapros == 3:
                    tovar = 'xerox'
                    print(Warehouse.max_stock_xerox)
                model = input(f'вы выбрали {tovar} \nостаток склада: {self.remains}\nНазовите необходимого производителя\n')
            except:
                return 'Некорректный ввод'
            try:
                col = int(input('кол-во техники'))
                if col < 10:
                    self.price = 4500
                    self.remains -= col
                elif 10 <= col <= 25:
                    self.price = 3500
                    self.remains -= col
                elif col > 25:
                    self.price = 3000
                    self.remains -= col
            except:
                return 'Некорректный ввод'
            try:
                self.remains -= col
                if self.remains < 0:
                    print('добавлено к заказу, ожидание уйдет 7-14 дней')
            except:
                return 'данный заказ можем осуществить через 7 дня'
            pozition = {'модель': model, 'кол-во': col}
            self.order.append(pozition)
            print(f'{self.order}, сумма заказа {self.price * col}р.')


class Warehouse:
    max_stock_printer = 6
    max_stock_scan = 8
    max_stock_xerox = 4
    def __init__(self):
        self.max_stock = 300


class Printer(OrgTeh):
    def printer_stock(self):
        try:
            print(f"Вместимость склада: {max_stock_printer}")
            col = int(input('Введите кол-во необходимой техники'))



class Scan(OrgTeh):
    pass


class Xerox(OrgTeh):
    pass



unit_1 = Printer('hp', 2000)
unit_2 = Scan('Canon', 1200)
unit_3 = Xerox('Xerox', 1500)
print(unit_2.realiz())
print(unit_3.realiz())
print(unit_1.realiz())

