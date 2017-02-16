
class BaseChar():
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    

    def __str__(self):
        return self.__class__.__name__