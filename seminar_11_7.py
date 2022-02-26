class ComplexNumbers:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'({self.num})'

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


a = ComplexNumbers(5 + 6j)
b = ComplexNumbers(3 + 1j)

print(a + b)
print(a * b)