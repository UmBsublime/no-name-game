import curses


from game.utils.observer import Observer
from game.events import move, death, attack


class StatusUI:
    def __init__(self, position, size):

        self.size_x = size.pos_x
        self.size_y = size.pos_y
        self.event_observer = StatusUI.EventObs(self)

        self.win = curses.newwin(self.size_x,
                                 self.size_y,
                                 position.pos_x,
                                 position.pos_y)
        self.win.box()
        self.win.clear()
        #self.update('Init')
        self.eventStruc = {move.MoveEvent: self.move,
                           death.DeathEvent: self.death,
                           attack.AttackEvent: self.attack}
    
    def move(self, event):
        t = "{} moves to {}".format(event.target.name, event.pos)
        self.update(t)
    def attack(self, event):
        return "{} attacks {}".format(event.src.name, event.dst.name)

    def death(self, event):
        pass

    def update(self, text):
        self.win.addstr(1, 1, text)

        self.win.box()
        self.win.refresh()
    def nothing(self, event):
        return "event_type not implemented"

    class EventObs(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):

            cmd = self.outer.eventStruc.get(type(arg), self.outer.nothing)
            cmd(arg)
