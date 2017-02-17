from os import system
from game.maps.map import Map, Position


def move(map ,player, direction):

    dst_pos = player
    if direction is'up':
        dst_pos = Position(player.pos_x-1, player.pos_y)
    elif direction is 'down':
        dst_pos = Position(player.pos_x + 1, player.pos_y)
    elif direction is'left':
        dst_pos = Position(player.pos_x, player.pos_y - 1)
    elif direction is'right':
        dst_pos = Position(player.pos_x, player.pos_y + 1)

    if map.try_move(player, dst_pos):
        map.do_move(player, dst_pos)
        return dst_pos

    return player


def map_demo():
    choices = {'w': 'up',
               'a': 'left',
               's': 'down',
               'd': 'right'}

    m = Map('./maps/map1.txt')
    hero_pos = Position(3, 5)

    while True:
        print(chr(27) + "[2J")
        m.print_map()
        for k,v in choices.items():
            print("{}: {}". format(v, k))
        selection = None
        while selection not in choices.keys():
            selection = system('read -p "your choice"')
            selection = input("Your choice: ")

        hero_pos = move(m, hero_pos, choices[selection])


def main():
    map_demo()

    

if __name__ == "__main__":
    main()