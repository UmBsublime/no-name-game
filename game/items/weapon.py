from .item import BaseItem

class Weapon(BaseItem):

    def __init__(self, dmg, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self._dmg = dmg

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        pass

#"Weapon"