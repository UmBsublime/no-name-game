from game.ui.term.map import MultiMapUI
from game.ui.term.player import PlayerUI
from game.maps.multimap import MultiMap
from game.maps.map import Position 
from game.actors.actor import BaseActor
from game.events.dispatcher import Dispatcher
from game.events.move import MoveEvent
import curses

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

    # Prep UI
    map_ui = MultiMapUI(mm, ui_pos)
    player_ui = PlayerUI(p1, Position(0, map_ui.size_y), Position(map_ui.size_x, 20))

    # Plug everything in event dispatcher
    eventd = Dispatcher(debug=False)
    eventd.moveNotifier.addObserver(map_ui.move_observer)
    eventd.moveNotifier.addObserver(p1.move_observer)
    eventd.moveNotifier.addObserver(e1.move_observer)
    eventd.moveNotifier.addObserver(player_ui.move_observer)

    # We check what we've got
    stdscr.getch()

    # Hero move down
    move(mm, p1_pos, 'down')
    new_pos = Position(4, 5)
    new_move = MoveEvent(p1, new_pos)
    eventd.move(new_move)
    stdscr.getch()

    # Enemy move down
    move(mm, e1_pos, 'down')
    new_pos = Position(6, 5)
    new_move = MoveEvent(e1, new_pos)
    eventd.move(new_move)
    stdscr.getch()



def move(map, player_pos, direction):

    dst_pos = player_pos
    if direction is'up':
        dst_pos = Position(player_pos.pos_x - 1, player_pos.pos_y)
    elif direction is 'down':
        dst_pos = Position(player_pos.pos_x + 1, player_pos.pos_y)
    elif direction is'left':
        dst_pos = Position(player_pos.pos_x, player_pos.pos_y - 1)
    elif direction is'right':
        dst_pos = Position(player_pos.pos_x, player_pos.pos_y + 1)

    if map.try_move(player_pos, dst_pos):
        return map.do_move(player_pos, dst_pos)
    return player_pos

def blah(text): print("\n{}\n* {:<27}*\n{}".format("=" * 30, text, "=" * 30))

if __name__ == "__main__":
    


    
    
    curses.wrapper(main)