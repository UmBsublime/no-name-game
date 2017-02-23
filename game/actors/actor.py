from game.utils.observer import Observer
from game.events import death, move, attack
class BaseActor():
    
    def __init__(self, name, hp, position):
        self.name = name
        self.hp = hp
        self.pos = position
        self._next_action = None


    def get_action(self):
        action = self._next_action
        self._next_action = None
        return action

    def set_next_action(self, action):
        '''
        populate self._next_action
        '''
        raise NotImplemented

    def get_stats(self):
        r =  {'name': self.name,
                'hp': self.hp,
                'pos': self.pos}
        return r


                    
    def __str__(self):
        return "{} -> {}".format(self.__class__.__name__, self.name)

