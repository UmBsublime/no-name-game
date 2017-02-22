import curses

from game.maps.multimap import MultiMap
from game.maps.multimap import Position
from game.utils.observer import Observer 
from game.events import move

class MultiMapUI:

    def __init__(self, multimap, position):
        self.mm = multimap
        self.size_x = self.mm.current_map.size_x
        self.size_y = self.mm.current_map.size_y
        self.move_observer = MultiMapUI.MoveObs(self)
        self.win = curses.newwin(self.mm.current_map.size_x,
                                 self.mm.current_map.size_y,
                                 position.pos_x,
                                 position.pos_y)
        self.win.box()
        self.win.clear()
        self.update()

    def update(self):
        #self.win.clear()
        for line in self.mm.current_map.map.keys():
            map_line = ''
            for column, value in self.mm.current_map.map[line].items():
                map_line += value.representation
            self.win.addstr(line - 1, 0, map_line)
        self.win.box()
        self.win.refresh()

    class MoveObs(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if type(arg) is move.MoveEvent:
                 self.outer.update()