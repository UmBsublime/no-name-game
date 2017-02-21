from game.maps.map import Position
from game.actors.player import BaseActor
from game.events.dispatcher import Dispatcher
from game.events  import move, death, attack

def blah(text):
    print("\n{}\n* {:<27}*\n{}".format("="*30, text, "="*30))



eventd = Dispatcher(debug=False)
p1 = BaseActor("Player_1", 10)
p2 = BaseActor("Player_2", 10)
p3 = BaseActor("Player_3", 10)
for i in [p1, p2, p3]:
    eventd.moveNotifier.addObserver(i.move_observer)
    eventd.attackNotifier.addObserver(i.attack_observer)
    #eventd.deathNotifier.addObserver(i.death_observer)


blah("trying move p1")
new_pos = Position(5,5)
new_move = move.MoveEvent(p1, new_pos)
eventd.move(new_move)

blah("p1 attack p2")
attack = attack.AttackEvent(p1, p2)
eventd.attack(attack)

blah("p2 dies")
death = death.DeathEvent(p2)
eventd.death(death)
eventd.moveNotifier.deleteObserver(p2.move_observer)
eventd.attackNotifier.deleteObserver(p2.attack_observer)
