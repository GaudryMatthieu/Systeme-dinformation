from abc import ABC, abstractmethod

class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass
    
class FlyNone(FlyBehaviour):
    def fly(self):
        return 'unable to fly'
    
class FlyInSpace(FlyBehaviour):
    def fly(self):
        return 'flying in the space'