from .char import BaseChar

class Npc(BaseChar):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def interact(self):
        pass