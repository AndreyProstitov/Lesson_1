class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, num):
        return str(self.number) + '\n' + ''.join([f'*\n' if (i + 1) % num == 0 else '*' for i in range(self.number)])


C_1 = Cell(42)
C_2 = Cell(3)

print((C_1 + C_2).make_order(5))
print((C_1 * C_2).make_order(4))
print((C_1 // C_2).make_order(5))
print((C_1 - C_2).make_order(5))