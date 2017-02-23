from game.utils.observer import Observable

class Dispatcher:
    def __init__(self, debug=False):
        self.debug = debug
        self.attackNotifier = Dispatcher.Attack(self)
        self.moveNotifier = Dispatcher.Move(self)
        self.deathNotifier = Dispatcher.Death(self)
        self.inputNotifier = Dispatcher.Input(self)

    def move(self, event):
        self.moveNotifier.notifyObservers(event)

    def attack(self, event):
        self.attackNotifier.notifyObservers(event)

    def death(self, event):
        self.deathNotifier.notifyObservers(event)

    class Attack(Observable):

        def __init__(self, outer):
            Observable.__init__(self, outer.debug)

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)
            self.clearChanged()

    class Move(Observable):
        def __init__(self, outer):
            Observable.__init__(self, outer.debug)

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)
            self.clearChanged()

    class Death(Observable):
        def __init__(self, outer):
            Observable.__init__(self, outer.debug)

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)
            self.clearChanged()

    class Input(Observable):
        def __init__(self, outer):
            Observable.__init__(self, outer.debug)

        def notifyObservers(self, event):
            self.setChanged()
            Observable.notifyObservers(self, event)
            self.clearChanged()