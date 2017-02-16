from .effect import BaseEffect

class Burn(BaseEffect):

    def __init__(self, effect_value):

        super().__init__(name="Burn")
        self.effect_value = effect_value