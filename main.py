#!/usr/bin/env python3

from game.chars.char import BaseChar

from game.chars.ennemy import Ennemy
from game.chars.player import Player

from game.scenes.scene import BaseScene


from game.items.item import BaseItem
from game.items.weapon import Weapon
from game.items.disposable import Disposable
from game.items.effect.heal import Heal
from game.items.inventory import Inventory


def main():
    b = BaseChar(10, 'dummy')
    i = BaseItem('stick', 5, 2)

    dagger = Weapon(5, 'Dagger', 5, 1)
    s_heal = Heal(10)
    s_potion = Disposable([s_heal], 'Small Potion', 10, 1)

    inv = Inventory(10,[dagger, s_potion])
    e = Ennemy(20, 'Looser')


    p = Player(1,2,3,4, inv, 100,"InterWiz")
    p.stats()

    s = BaseScene('map', p)



if __name__ == "__main__":
    main()
