from duck import Duck

class Goose:
    def __init__(self, sexe : str = 'M', color : str = "white"):
        self.__sexe = sexe
        self.__color = color
    
    def goose_fly(self):
        return f'fly'
    
    def honk(self):
        return f'honk honk !!'

class GooseAsDuck(Duck):
    def __init__(self, goose : Goose):
        super().__init__('White', 'M')
        self.__goose = goose
            
    def fly(self):
        return self.__goose.goose_fly()
        
    def quack(self):
        return self.__goose.honk()
        
    def display(self):
        return super().display()

