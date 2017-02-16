from .char import BaseChar
from ..items.inventory import BaseInventory

class Player(BaseChar):

    def __init__(self, dex, agl, str, lck, inventory, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.dex = dex
        self.agl = agl
        self.str = str
        self.lck = lck
        self.inventory = inventory
        self.left_hand = BaseInventory(1)
        self.right_hand = BaseInventory(1)

    def stats(self):
        f = "Name:..{}\n" \
            "Dex:...{}\n" \
            "Agl:...{}\n" \
            "Str:...{}\n" \
            "Lck:...{}\n\n" \
            "Inventory:"
        print(f.format(self.name, self.dex, self.agl, self.str, self.lck))
        self.inventory.show_content()

