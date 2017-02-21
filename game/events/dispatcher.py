from game.utils.observer import Observable

class Dispatcher:
    def __init__(self):
        self.attackNotifier = Dispatcher.Attack(self)
        self.moveNotifier = Dispatcher.Move(self)
        self.deathNotifier = Dispatcher.Death(self)

    def move(self, event):
        self.moveNotifier.notifyObservers(event)

    def attack(self, event):
        self.attackNotifier.notifyObservers(event)

    def death(self, event):
        self.deathNotifier.notifyObservers(event)

    class Attack(Observable):

        def __init__(self, outer):
            Observable.__init__(self)

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)

    class Move(Observable):
        def __init__(self, outer):
            Observable.__init__(self)

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)

    class Death(Observable):
        def __init__(self, outer):
            Observable.__init__(self)

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)