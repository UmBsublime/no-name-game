from curses import wrapper

from collections import OrderedDict

from game.ui.term.map import MultiMapUI
from game.ui.term.player import PlayerUI
from game.ui.term.status import StatusUI
from game.ui.term.menu import MenuUI, Menu
from game.ui.term.input import InputHandler
from game.maps.multimap import MultiMap
from game.maps.map import Position
from game.actors.actor import BaseActor
from game.events.dispatcher import Dispatcher
from game.events.move import MoveEvent

def main(stdscr):

    stdscr.refresh()

    # Prep actors
    ui_pos = Position(0, 0)
    p1_pos = Position(3, 5)
    e1_pos = Position(5, 5)
    p1 = BaseActor('hero', 10, p1_pos)
    e1 = BaseActor('enemy', 10, e1_pos)

    # Prep map
    map_file_struc = {1: {1: './maps/multimap_1_1.txt',
                          2: './maps/multimap_1_2.txt'},
                      2: {1: './maps/multimap_2_1.txt',
                          2: './maps/multimap_2_2.txt'}}
    mm = MultiMap(map_file_struc)
    mm.add_actor(e1_pos, '%')

    # Prep menu
    menu = Menu("Type key:", OrderedDict([("w", "Up"), ("a", "Left"), ("s", "Down"), ("d", "Right"), ("q", "Quit")]))

    # Prep UI
    map_ui = MultiMapUI(mm, ui_pos)
    player_ui = PlayerUI(p1,
                         Position(int(map_ui.size_x / 2), 20),
                         Position(0, map_ui.size_y))
    menu_ui = MenuUI(menu,
                     Position(int(map_ui.size_x / 2), 20),
                     Position(int(map_ui.size_x / 2), map_ui.size_y))
    status_ui = StatusUI(Position(1, map_ui.size_y + player_ui.size_y),
                         Position(map_ui.size_x, 0))

    menu_ui.start()
    # Plug everything in event dispatcher
    eventd = Dispatcher(debug=False)
    eventd.moveNotifier.addObserver(map_ui.move_observer)
    eventd.moveNotifier.addObserver(player_ui.move_observer)
    eventd.moveNotifier.addObserver(status_ui.event_observer)

    # Prep event handler
    input_handler = InputHandler({"w": MoveEvent(p1, 'up'),
                                  "a": MoveEvent(p1, 'left'),
                                  "s": MoveEvent(p1, 'down'),
                                  "d": MoveEvent(p1, 'right'),
                                  "q": 'quit'}, stdscr.getch)

    # EZPZ game loop
    while True:
        k = input_handler.get_key()
        if k is 'quit':
            exit()
        elif k is not None:
            eventd.move(k)
    return repr(k)

if __name__ == "__main__":

    r = wrapper(main)
    print(repr(r))