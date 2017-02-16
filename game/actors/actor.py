
class BaseActor():
    
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self._next_action = None

    def get_action(self):
        action = self._next_action
        self._next_action = None
        return action

    def set_next_action(self):
        '''
        populate self._next_action
        '''
        raise NotImplemented


