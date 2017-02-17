#!/usr/bin/env python3

from game.actors.actor import BaseActor
from game.actors.ennemy import Ennemy
from game.actors.player import Player
from game.effects.heal import Heal
from game.items.disposable import Disposable
from game.items.inventory import BaseInventory
from game.items.item import BaseItem
from game.items.weapon import Weapon
from game.maps.map import Map


def main():

    b = BaseActor(10, 'dummy')
    i = BaseItem('stick', 5, 2)

    dagger = Weapon(5, 'Dagger', 5, 1)
    s_heal = Heal(10)
    s_potion = Disposable([s_heal], 'Small Potion', 10, 1)

    inv = BaseInventory(10,[dagger, s_potion])
    e = Ennemy(20, 'Looser')


    p = Player(1,2,3,4, inv, 100,"InterWiz")
    p.stats()
    _test_map()
    #s = BaseScene('map', p)


def _test_map():
    from game.maps.map import Map, Position
    m = Map('./maps/map1.txt')
    src_pos = Position(3, 5)
    dst_pos = Position(6, 6)
    m.try_move(src_pos, dst_pos)
    m.do_move(src_pos, dst_pos)
    m.print_map()


if __name__ == "__main__":
    main()
