class BaseEffect():

    def __init__(self, name):

        self.name = name

    def __str__(self):
        return self.__class__.__name__