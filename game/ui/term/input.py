import curses
from game.utils.observer import Observer

class InputHandler:
    
    def __init__(self, input_mapping, get_key_func):
        self.get_key_func = get_key_func
        self.input_mapping = input_mapping

    def get_key(self):
        key = chr(self.get_key_func())
        if key in self.input_mapping.keys():
            
            event = self.input_mapping.get(key, None)
            return event
        return None
