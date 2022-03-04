import time


class TrafficLight:
    __color: dict = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        for color, time_on in self.__color.items():
            print(f'{color} {time_on} сек')
            time.sleep(time_on)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
