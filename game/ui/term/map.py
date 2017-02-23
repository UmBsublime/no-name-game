import curses

from game.maps.multimap import MultiMap
from game.maps.multimap import Position
from game.utils.observer import Observer 
from game.events import move

class MultiMapUI:

    def __init__(self, multimap, position):
        self.mm = multimap
        self.size_x = self.mm.current_map.size_x + 1
        self.size_y = self.mm.current_map.size_y + 1
        self.move_observer = MultiMapUI.MoveObs(self)
        self.win = curses.newwin(self.size_x,
                                 self.size_y,
                                 position.pos_x,
                                 position.pos_y)
        self.win.box()
        self.win.clear()
        self.update()

    def move(self, arg):

        if arg.direction is 'up':
            dst_pos = Position(arg.target.pos.pos_x - 1, arg.target.pos.pos_y)
        elif arg.direction is 'down':
            dst_pos = Position(arg.target.pos.pos_x + 1, arg.target.pos.pos_y)
        elif arg.direction is 'left':
            dst_pos = Position(arg.target.pos.pos_x, arg.target.pos.pos_y - 1)
        elif arg.direction is 'right':
            dst_pos = Position(arg.target.pos.pos_x, arg.target.pos.pos_y + 1)

        ret_val = arg.target.pos
        if self.mm.try_move(arg.target.pos, dst_pos):
            ret_val = self.mm.do_move(arg.target.pos, dst_pos)
        arg.target.pos = ret_val
        self.update()
        return ret_val
    
    def update(self):
        
        for line in self.mm.current_map.map.keys():
            map_line = ''
            for column, value in self.mm.current_map.map[line].items():
                map_line += value.representation
            self.win.addstr(line, 1, map_line)
        self.win.box()
        self.win.refresh()

    class MoveObs(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if type(arg) is move.MoveEvent:
                 self.outer.move(arg)