

from game.maps.map import Position
from game.actors.player import BaseActor
from game.events.dispatcher import Dispatcher
from game.events  import move, death, attack

def blah(text):
    print("{}\n| {}\n{}".format("="*30, text, "="*30))
    
    

eventd = Dispatcher()
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
#eventd.attackNotifier.addObserver(p2.attack_observer)
#eventd.moveNotifier.addObserver(p2.move_observer)
# Register who needs to watch what



#f.mapNotifier.addObserver(p1.move_observer)
#f.eventNotifier.addObserver(p1.move_observer)

#f.mapNotifier.addObserver(p2.move_observer)
#f.eventNotifier.addObserver(p2.event_observer)

#ui_main = UI("Main_UI")
#f.eventNotifier.addObserver(ui_main.event_observer)
#f.mapNotifier.addObserver(ui_main.map_observer)

#ui_map = UI("Map_UI")
#f.mapNotifier.addObserver(ui_map.map_observer)


# Engine can now notify all relevant obeservers when something happens
'''
# A change that interests observers:
blah('p1 moves')
f.map_changed(p1)
blah("p2 moves")
f.map_changed(p2)
# p1 attacks p2
blah("p1 attacks p2")
att_event = AttackEvent(p1, p2)
f.event(att_event)

# player 2 dies
blah('p2 death')
p2_death_event = DeathEvent(p2)
f.event(p2_death_event)
f.mapNotifier.deleteObserver(p2.map_observer)
f.eventNotifier.deleteObserver(p2.event_observer)


#f.event(AttackEvent())
blah("p1 moves again")
f.map_changed(p1) # It's already open, no change.
# Bee 1 doesn't want to go to bed:

#f.eventNotifier.deleteObserver(p1.map_observer)
#f.map_no_change()
##f.close() # It's already closed; no change
#f.openNotifier.deleteObservers()
#f.open()
#f.close()
'''