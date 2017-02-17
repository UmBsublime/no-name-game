DURATION = 100 #ms
ENERGY_POINTS = 5

from ..maps.map import Map
from ..actions import Walk

KEYMAP = {'w': Walk('up'),
          'a': Walk('left'),
          's': Walk('down'),
          'd': Walk('right')}


class Engine():

    def __init__(self, config):
        #self.player = config['player']
        self.map = config['Map']
        self.input_source = config['Input_Source']
        self.actors = self.map.get_actors()
        self._current_actor = 0

    def process(self):

        if self.actors[self._current_actor].__str__() == 'Player':
            self.actors[self._current_actor].set_next_action(self.handle_input(self.input_source))
        self.actors[self._current_actor].get_action()
        action = self.actors[self._current_actor].get_action()
        if action is None:
            return

        while True:
            result = action.perform()
            if not result.succeeded:
                return
            if result.alternate is None:
                break
            action = result.alternate

        self._current_actor = (self._current_actor + 1) % len(self.actors)


    def _init_actors(self):
        actors = []
        for tile in self.map:
            if tile.type == 'Actor':
                actors.append(generate_actor(tile))

    def handle_input(self, input_source):
        while True:
            current_input = input_source.get_input()
            if current_input in KEYMAP.keys():
                self.actors[self._current_actor].set_next_action(KEYMAP[current_input])

def generate_actor(tile):

    raise NotImplemented
