class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = _income


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}, {self.position}')

    def get_total_income(self):
        zp = 0
        for key, val in self.income.items():
            zp += val
            print(f'{key} - {val}')
        print(zp)


income = {"wage": 232333, "bonus": 343433}
a = Position("Andrey", "Prostitov", 'God', income)
a.get_full_name()
a.get_total_income()
