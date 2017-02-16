class BaseInputSource():

    def get_input(self):
        raise NotImplemented

class Keyboard(BaseInputSource):

    def get_input(self):
        return input('What key: ')
