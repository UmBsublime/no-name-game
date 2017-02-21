from game.utils.observer import Observer, Observable


class Engine:

    def __init__(self):

        self.mapNotifier = Engine.MapNotifier(self)
        self.eventNotifier= Engine.EventNotifier(self)

    def map_changed(self, target): # Map has changed
        self.mapNotifier.notifyObservers(target)

    def event(self, event): # Map has changed
        self.eventNotifier.notifyObservers(event)

    class MapNotifier(Observable):
        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer

        def notifyObservers(self, target):
            self.setChanged()
            Observable.notifyObservers(self, target)

    class EventNotifier(Observable):

        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)

class EventNotifier:
    def __init__(self):
        self.attackNotifier = EventNotifier.AttackNotifier(self)

    class AttackNotifier(Observable):

        def __init__(self, outer):
            Observable.__init__(self)

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)

class Player:
    def __init__(self, name):
        self.name = name
        self.map_observer = Player.MapObserver(self)
        self.event_observer = Player.EventObserver(self)

    class MapObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if arg is self.outer:
                print("Player " + self.outer.name + " updated his position")

    class EventObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if type(arg) is AttackEvent:
                if arg.src is self.outer:
                    print("Player " + self.outer.name + " is ready to attack")
                if arg.target is self.outer:
                    print("Player " + self.outer.name + " is ready to defend")
            if type(arg) is DeathEvent:
                if arg.target is self.outer:
                    print("Player " + self.outer.name + " is dead")

class UI:

    def __init__(self, name):
        #self.name = name
        self.map_observer = UI.MapObserver(self)
        self.event_observer = UI.EventObserver(self)

    class MapObserver(Observer):

        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):

            print("UI has updated map")

    class EventObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            if type(arg) is AttackEvent:
                print("UI will update Health tab")

class AttackEvent():
    def __init__(self, src, target):
        self.src = src
        self.target = target
        pass

class DeathEvent():
        def __init__(self, target):
            self.target = target




def blah(text):
    print("{}\n| {}\n{}".format("="*30, text, "="*30))
    
    
blah("Create engine")
f = Engine()

# Register who needs to watch what
p1 = Player("Hero_1")
f.mapNotifier.addObserver(p1.map_observer)
f.eventNotifier.addObserver(p1.event_observer)

p2 = Player("Hero_2")
f.mapNotifier.addObserver(p2.map_observer)
f.eventNotifier.addObserver(p2.event_observer)

ui_main = UI("Main_UI")
f.eventNotifier.addObserver(ui_main.event_observer)
f.mapNotifier.addObserver(ui_main.map_observer)

ui_map = UI("Map_UI")
f.mapNotifier.addObserver(ui_map.map_observer)


# Engine can now notify all relevant obeservers when something happens

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