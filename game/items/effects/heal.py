from .effect import BaseEffect

class Heal(BaseEffect):

    def __init__(self, effect_value):

        super().__init__(name="Heal")
        self.effect_value = effect_value