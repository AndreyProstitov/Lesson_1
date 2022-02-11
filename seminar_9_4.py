from random import choice


class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Auto {self.name}-{self.color} star")

    def stop(self):
        print(f"Auto {self.name}-{self.color} stop")

    def turn(self, direction):
        print((f'{self.name} {direction}'))

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def pol(self):
        if self.is_police:
            print("Это авто полиции")


direction = ["Повернула направо", "Повернула налево", "Выполнила разворот"]

Police = WorkCar(66, 'Black', 'AUDI', True)
Police.go()
Police.show_speed()
for i in range(2):
    Police.turn(choice(direction))
Police.stop()
aaa = PoliceCar(22, 'Black', 'AU', True)
aaa.pol()
