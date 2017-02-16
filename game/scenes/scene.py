class BaseScene():

    def __init__(self, map, player):
        self.map = map
        self.players = player
        try:
            self.prepare_scene()
        except:
            pass

    def prepare_scene(self):
        pass

    def update(self):
        pass

    def next_turn(self):
        pass

    def refresh(self):
        pass

    def __str__(self):
        return self.__class__.__name__