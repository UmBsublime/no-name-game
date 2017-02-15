from .item import BaseItem

class Weapon(BaseItem):

    def __init__(self, dmg, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.dmg = dmg

    def get_dmg(self):
        pass

    def __str__(self):
        return "Weapon"