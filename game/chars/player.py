from .char import BaseChar

class Player(BaseChar):

    def __init__(self, dex, agl, str, lck, inventory, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.dex = dex
        self.agl = agl
        self.str = str
        self.lck = lck
        self.inventory = inventory

    def stats(self):
        f = "Name:..{}\n" \
            "Dex:...{}\n" \
            "Agl:...{}\n" \
            "Str:...{}\n" \
            "Lck:...{}\n\n" \
            "Inventory:"
        print(f.format(self.name, self.dex, self.agl, self.str, self.lck))
        self.inventory.show_content()

