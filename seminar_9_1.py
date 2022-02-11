from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__collor = color

    def running(self):
        while True:
            for key, val in self.__collor.items():
                print(key)
                sleep(val)


traf_dict = {"\033[31m Red": 7, "\033[33m Yellow": 2, "\033[32m Green": 3}
asd = TrafficLight(traf_dict)
asd.running()