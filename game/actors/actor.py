from game.utils.observer import Observer
from game.events import death, move, attack
class BaseActor():
    
    def __init__(self, name, hp, position):
        self.name = name
        self.hp = hp
        self.pos = position
        self._next_action = None
        self.move_observer = BaseActor.MoveObs(self)
        self.attack_observer = BaseActor.AttackObs(self)

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

    def get_attacked(self, src):
        print("Player {} is ready to defend from {}".format(self.name, src.name))

    def attack(self, dst):
        print("Player {} is ready to attack {}".format(self.name, dst.name))

    def death(self):
        print("Player {} dies...".format(self.name))

    def move(self, new_pos):
        self.pos = new_pos
        #print("Player {} moved to {}".format(self.name, new_pos))

    class MoveObs(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if type(arg) is move.MoveEvent:

                if arg.target is self.outer:
                    self.outer.move(arg.pos)

    class DeathObs(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if type(arg) is death.DeathEvent:

                if arg.target is self.outer:
                    self.outer.death()

    class AttackObs(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if type(arg) is attack.AttackEvent:
                if arg.src is self.outer:
                    self.outer.attack(arg.dst)
                if arg.dst is self.outer:
                    self.outer.get_attacked(arg.src)
                    
    def __str__(self):
        return "{} -> {}".format(self.__class__.__name__, self.name)

