import curses


from game.utils.observer import Observer
from game.events import move, death, attack


class StatusUI:
    def __init__(self, size, position):
        
        self.size_x = size.pos_x + 2
        self.size_y = size.pos_y 
        self.event_observer = StatusUI.EventObs(self)

        self.content = []
        for i in range(size.pos_x):
            self.content.append('')

        self.win = curses.newwin(self.size_x,
                                 self.size_y,
                                 position.pos_x,
                                 position.pos_y)
        self.win.box()
        self.win.clear()
        #welcome = "{space}{text}{space}".format(space=' ' * (self.size_x - 2))
        self.update('Welcome')
        self.eventStruc = {move.MoveEvent: self.move,
                           death.DeathEvent: self.death,
                           attack.AttackEvent: self.attack}
        
    
    def move(self, event):
        t = "{} moved {}".format(event.target.name, event.direction)
        self.update(t)
    def attack(self, event):
        return "{} attacks {}".format(event.src.name, event.dst.name)

    def death(self, event):
        pass
    
    def clear(self):
        clear_str = ' ' * self.size_y
        line = 1
        for i in self.content:
            self.win.addstr(line, 1, clear_str)
            line += 1

    def update(self, text):
        #clear_str = ' ' * self.size_y
        #self.win.addstr(1,0, clear_str)
        self.clear()
        self.content.pop(0)
        self.content.append(text)
        line = 1
        for i in self.content:
            self.win.addstr(line, 1, i)
            line += 1

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
