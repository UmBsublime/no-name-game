import curses

from game.maps.multimap import MultiMap
from game.maps.multimap import Position
from game.utils.observer import Observer 
from game.events import move

class PlayerUI:

    def __init__(self, player, position, size):
        self.player = player
        self.size_x = size.pos_x
        self.size_y = size.pos_y
        self.move_observer = PlayerUI.MoveObs(self)
        
        self.win = curses.newwin(self.size_x,
                                 self.size_y,
                                 position.pos_x,
                                 position.pos_y)
        self.win.box()
        self.win.clear()
        self.update()

    def update(self):
        line = 1
        f = '* {} {}'
        for k, v in self.player.get_stats().items():
            t = f.format(k, v)
            self.win.addstr(line, 1, t)
            line += 1
        self.win.box()
        self.win.refresh()

    class MoveObs(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if type(arg) is move.MoveEvent:
                if arg.target is self.outer.player:
                    self.outer.update()