#!/usr/bin/env python3

from game.char.char import BaseChar

from game.char.ennemy import Ennemy
from game.char.player import Player

from game.scene.scene import BaseScene


from game.item.item import BaseItem
from game.item.weapon import Weapon
from game.item.disposable import Disposable
from game.item.effect.heal import Heal
from game.item.inventory import Inventory


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



if __name__ == "__main___":
    print('main')
    main()
main()