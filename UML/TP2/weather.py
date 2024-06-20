from random import randrange, randint
from abc import abstractmethod, ABC

class Display:
    
    @abstractmethod
    def update_display(self, temperature, pressure, humidity):
        pass

class Observer(ABC):
    
    @abstractmethod
    def notify(self):
        pass

class DisplayTemp(Display, Observer):
    def update_display(self, temperature, pressure, humidity):
        print(f'temperature: {temperature}')

    def notify(self):
        print('temperature:')

class DisplayPressure(Display, Observer):
    def update_display(self, temperature, pressure, humidity):
        print(f'pressure: {pressure}')

    def notify(self):
        print('pressure')

class DisplayHumidity(Display, Observer):
    def update_display(self, temperature, pressure, humidity):
        print(f'humidity: {humidity}')

    def notify(self):
        print('humidity')

class DisplayLolCat(Display, Observer):
    def update_display(self, temperature, pressure, humidity):
        print(f'Lol Cat: {temperature} vs {pressure}')

    def notify(self):
        print('lol cat')

class Subject:
    def __init__(self):
        self.__observers = []

    def register_observer(self, observer : Observer):
        self.__observers.append(observer)

    def unregister_observer(self, observercls):
        self.__observers = [observer for observer in self.__observers if not isinstance(observer, observercls)]

    def notifiy_observers(self):
        for observer in self.__observers:
            observer.notify()

class WeatherData(Subject):

    def __init__(self):
        super().__init__()
        self.register_observer(DisplayHumidity())
        self.register_observer(DisplayPressure())
        self.register_observer(DisplayTemp())

    def get_temperature(self):
        return randrange(-20, 50)

    def get_pressure(self):
        return randint(800, 1100)

    def get_humidity(self):
        return randrange(0, 100)

    def measurements_changed(self):
        
        # collect measures
        temperature = self.get_temperature()
        pressure = self.get_pressure()
        humidity = self.get_humidity()

        self.notifiy_observers()

if __name__ == '__main__':
    w = WeatherData()
    print('==================')
    w.measurements_changed()
    print('==================')
    w.register_observer(DisplayLolCat())
    w.unregister_observer(DisplayHumidity)
    w.measurements_changed()