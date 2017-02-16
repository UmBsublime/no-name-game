class BaseItem():
    def __init__(self, name, value, size):
        self.name = name
        self.value = value
        self.size = size


    def __str__(self):
        return self.__class__.__name__