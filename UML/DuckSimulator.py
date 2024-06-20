from duck import Donald, Duck
from goose import Goose, GooseAsDuck

class DuckSimulator:
    
    def __init__(self):
        self.__ducks = []
        
    def enroll_duck(self, duck : Duck):
        if isinstance(duck, Duck):
            self.__ducks.append(duck)
        else :
            raise TypeError('Virus detected')
                
    def simulate(self):
        for duck in self.__ducks:
           print(duck.fly())
           print(duck.fly())
           print(duck.quack())
           print(duck.fly())
           print(duck.fly())
           print(duck.fly())
                
if __name__ == "__main__":
    sim = DuckSimulator()
    sim.enroll_duck(Donald('green', 'M'))
    sim.enroll_duck(GooseAsDuck(Goose()))
    sim.simulate()