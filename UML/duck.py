# Cette import permet d'empecher une classe d'être instancier 
# Il faut juste faire hériter abc à la classe souhaitée
from abc import ABC, abstractmethod
from fly import FlyBehaviour, FlyInSpace, FlyNone
from quack import QuackBehaviour, LittleQuack, BigQuack

class Duck(ABC):    
    def __init__(self, color, sexe, fly_behaviour : FlyBehaviour = FlyNone(), quack_behaviour : QuackBehaviour = LittleQuack()):
        self.__color = color
        self.__sexe = sexe
        self.__fly_behaviour = fly_behaviour
        self.__quack_behaviour = quack_behaviour
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value
        
    @property
    def sexe(self):
        return self.__sexe
    
    @sexe.setter
    def sexe(self, value):
        self.__sexe = value
        
    @property
    def fly_behaviour(self):
        return self.__fly_behaviour
    
    @fly_behaviour.setter
    def fly_behaviour(self, value):
        self.__fly_behaviour = value
        
    @property
    def quack_behaviour(self):
        return self.__quack_behaviour
    
    @quack_behaviour.setter
    def quack_behaviour(self, value):
        self.__quack_behaviour = value
        
    def fly(self):
        return self.__fly_behaviour.fly()
        
    def quack(self):
        return self.__quack_behaviour.quack()
        
    @abstractmethod
    def display(self):
        return "look at me"
    
class Donald(Duck):
    def __init__(self, color, sexe):
        super().__init__(color, sexe)
    
    def display(self):
        return super().display()

class Picsou(Duck):
    def __init__(self, color, sexe, fly_behaviour: FlyBehaviour = FlyInSpace()):
        super().__init__(color, sexe, fly_behaviour)
    
    def display(self):
        return super().display()



def main():
    donald = Donald("vert", "M")
    picsou = Picsou("jaune", "M")
    print(donald.quack())
    print(picsou.quack())
    
    donald.quack_behaviour = BigQuack()
    print(donald.quack())

if __name__ == '__main__':
    main()