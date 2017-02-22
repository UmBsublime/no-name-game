from collections import OrderedDict
from .map import FloorTile

from .map import Map, Position

map_file_struc = {1: {1: './maps/multimap_1_1.txt',
                      2: './maps/multimap_1_2.txt'},
                  2: {1: './maps/multimap_2_1.txt',
                      2: './maps/multimap_2_2.txt'}}
class MultiMap():

    def __init__(self, map_path_struc):
        self.path_struc = map_path_struc
        self.multimap = self._prepare_multimap()
        self.size_x = len(self.multimap.keys()) + 1
        self.size_y = len(self.multimap[1].keys()) + 1

        self._current_pos = Position(1,1)
        self.current_map = self._map_at_pos(self._current_pos)

    def _prepare_multimap(self):
        multimap = OrderedDict()
        for line in self.path_struc.keys():
            multimap[line] = OrderedDict()
            for column in self.path_struc[line].keys():
                multimap[line][column] = Map(self.path_struc[line][column])

        return multimap

    def add_actor(self, pos, representation='%'):
        self.current_map.add_actor(pos, representation)

    def print_map(self):
        self.current_map.print_map()

    def try_move(self, src_pos, dst_pos):
        if self.current_map.try_move(src_pos, dst_pos) == 'OutOfBounds':
            #print("OutOfBounds")

            direction = self._find_direction(src_pos, dst_pos)
            return self._try_multimap_move(src_pos, direction)
        return self.current_map.try_move(src_pos, dst_pos)

    def do_move(self, src_pos, dst_pos):
        if self.current_map.try_move(src_pos, dst_pos) is True:

            self.current_map.do_move(src_pos, dst_pos)
            new_pos = dst_pos
        else:
            #print("Doing move")
            direction = self._find_direction(src_pos, dst_pos)
            src_tile = self.current_map._get_tile_at_pos(src_pos)
            
            backup_map = self.current_map
            if direction == 'left':
                self._current_pos = Position(self._current_pos.pos_x, self._current_pos.pos_y - 1)
                self.current_map = self._map_at_pos(self._current_pos)
                new_map_x = src_pos.pos_x
                new_map_y = list(self.current_map.map[src_pos.pos_x].keys())[-1]
            if direction == 'right':
                self._current_pos = Position(self._current_pos.pos_x, self._current_pos.pos_y + 1)
                self.current_map = self._map_at_pos(self._current_pos)
                new_map_x = src_pos.pos_x
                new_map_y = list(self.current_map.map[src_pos.pos_x].keys())[0]
            if direction == 'up':
                self._current_pos = Position(self._current_pos.pos_x - 1, self._current_pos.pos_y)
                self.current_map = self._map_at_pos(self._current_pos)
                new_map_x = list(self.current_map.map.keys())[-1]
                new_map_y = src_pos.pos_y
            if direction == 'down':
                self._current_pos = Position(self._current_pos.pos_x + 1, self._current_pos.pos_y)
                self.current_map = self._map_at_pos(self._current_pos)
                new_map_x = list(self.current_map.map.keys())[0]
                new_map_y = src_pos.pos_y
            new_pos = Position(new_map_x, new_map_y)
            #print(new_pos)
            #backup_map._set_tile_at_pos()
            dst_tile = self.current_map._get_tile_at_pos(new_pos)
            backup_map._set_tile_at_pos(dst_tile, src_pos)
            self.current_map._set_tile_at_pos(src_tile, new_pos)
        return new_pos

    def _map_at_pos(self, pos):
        return self.multimap[pos.pos_x][pos.pos_y]

    def _find_direction(self, src_pos, dst_pos):
        if src_pos.pos_x > dst_pos.pos_x:
            return 'up'
        if src_pos.pos_x < dst_pos.pos_x:
            return 'down'
        if src_pos.pos_y > dst_pos.pos_y:
            return 'left'
        if src_pos.pos_y < dst_pos.pos_y:
            return 'right'
        return 'none'

    def _try_multimap_move(self, src_pos, direction):
        #print("We are trying to go: {}".format(direction))

        try:
            if direction == 'left':
                map = self._map_at_pos(Position(self._current_pos.pos_x, self._current_pos.pos_y - 1))
                test_x = src_pos.pos_x
                test_y = list(map.map[src_pos.pos_x].keys())[-1]
            if direction == 'right':
                map = self._map_at_pos(Position(self._current_pos.pos_x, self._current_pos.pos_y + 1))
                test_x = src_pos.pos_x
                test_y = list(map.map[src_pos.pos_x].keys())[0]
            if direction == 'up':
                map = self._map_at_pos(Position(self._current_pos.pos_x - 1, self._current_pos.pos_y))
                test_x = list(map.map.keys())[-1]
                test_y = src_pos.pos_y
            if direction == 'down':
                map = self._map_at_pos(Position(self._current_pos.pos_x + 1, self._current_pos.pos_y))
                test_x = list(map.map.keys())[0]
                test_y = src_pos.pos_y
            return map.check_pos(Position(test_x, test_y))
        except KeyError:
            #print("we got an exception")
            return False
