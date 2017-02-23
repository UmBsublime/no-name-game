import curses

from game.utils.observer import Observer

class MenuUI:
    def __init__(self, menu, size, position):
        self.menu = menu
        self.size_x = size.pos_x
        self.size_y = size.pos_y
        #self.input_observer = MenuUI.InputObs(self)

        self.win = curses.newwin(self.size_x,
                                 self.size_y,
                                 position.pos_x,
                                 position.pos_y)
        self.active = False

    def prep(self):
        self.win.box()
        self.win.clear()
        self.active = True
        self.update()

        self.win.box()
        self.win.refresh()

    def update(self):
        if self.active:
            line = 1
            self.win.addstr(line, 1, self.menu.title)
            for key, action in self.menu.content.items():
                line += 1
                t = " * {}: {}".format(key, action)
                self.win.addstr(line, 1, t)

    def start(self):
        if not self.active:
            self.prep()
            self.active = True

    def stop(self):
        self.active = False

    class InputObs(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if self.active:
                pass
        
class Menu:
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        