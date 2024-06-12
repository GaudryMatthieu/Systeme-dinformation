from abc import ABC, abstractmethod

class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass
    
class LittleQuack(QuackBehaviour):
    def quack(self):
        return 'Coin'
    
class BigQuack(QuackBehaviour):
    def quack(self):
        return 'Coin coin coin coin'