class Stationery:
    def __init__(self, titles):
        self.title = titles

    def draw(self):
        print("запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")



class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}")


Pen_1 = Pen("ручкой")
Pen_1.draw()
Pensil_1 = Pencil("карандашом")
Pensil_1.draw()
Handle_1 = Handle("маркером")
Handle_1.draw()