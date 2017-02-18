from os import system
from game.maps.map import Map, Position
from game.maps.multimap import MultiMap


def move(map ,player, direction):

    dst_pos = player
    if direction is'up':
        dst_pos = Position(player.pos_x - 1, player.pos_y)
    elif direction is 'down':
        dst_pos = Position(player.pos_x + 1, player.pos_y)
    elif direction is'left':
        dst_pos = Position(player.pos_x, player.pos_y - 1)
    elif direction is'right':
        dst_pos = Position(player.pos_x, player.pos_y + 1)

    if map.try_move(player, dst_pos):
        return map.do_move(player, dst_pos)


    return player


def map_demo():
    choices = {'w': 'up',
               'a': 'left',
               's': 'down',
               'd': 'right'}

    m = Map('./maps/map1.txt')
    map_file_struc = {1: {1: './maps/multimap_1_1.txt',
                          2: './maps/multimap_1_2.txt'},
                      2: {1: './maps/multimap_2_1.txt',
                          2: './maps/multimap_2_2.txt'}}
    mm = MultiMap(map_file_struc)
    hero_pos = Position(3, 5)

    while True:
        from os import system
        #print(chr(27) + "[2J")
        system("clear")
        mm.print_map()
        for k,v in choices.items():
            print("{}: {}". format(v, k))
        selection = None
        while selection not in choices.keys():
            #selection = system('read -p "your choice"')
            selection = input("Your choice: ")

        hero_pos = move(mm, hero_pos, choices[selection])


import curses
from curses.textpad import Textbox, rectangle
map_file_struc = {1: {1: './maps/multimap_1_1.txt',
                          2: './maps/multimap_1_2.txt'},
                      2: {1: './maps/multimap_2_1.txt',
                          2: './maps/multimap_2_2.txt'}}
mm = MultiMap(map_file_struc)


def curses_test(stdscr):
    hero_pos = Position(3, 5)
    
    #stdscr.clear()

    mapscr = curses.newwin(100,100,0,0)
    stdscr.refresh()
    refresh_map(mapscr, mm)
    
    choices = {'w': 'up',
               'a': 'left',
               's': 'down',
               'd': 'right',
               'q': 'quit'}
    c = ord(' ')
    while True:
        c = stdscr.getch()
        while chr(c) not in choices.keys():
            c = stdscr.getch()
        if c == ord('q'):
            break
        hero_pos = move(mm, hero_pos, choices[chr(c)])
        refresh_map(mapscr, mm)
def refresh_map(win, mm):
    win.clear()
    for line in mm.current_map.map.keys():
        map_line = ''
        for column, value in mm.current_map.map[line].items():
            map_line += value.representation
        win.addstr(line - 1, 0, map_line)
    win.addstr(line + 2, 0, "'q' to quit")
    win.addstr(line + 3, 0, "'w' up")
    win.addstr(line + 4, 0, "'a' left")
    win.addstr(line + 5, 0, "'s' down")
    win.addstr(line + 6, 0, "'d' right")
    win.refresh()

def main():
    
    #map_demo()
    #stdscr = curses.initscr()
    #curses.noecho()
    #curses.cbreak()
    #stdscr.keypad(True)
    
    
    curses.wrapper(curses_test)

    

if __name__ == "__main__":
    main()