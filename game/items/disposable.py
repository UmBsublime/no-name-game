from .item import BaseItem

class Disposable(BaseItem):

    def __init__(self, effects, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.effects = effects


    def consume(self):
        pass
