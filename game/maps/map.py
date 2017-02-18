from collections import OrderedDict
from .tile import ActorTile, WallTile, FloorTile, BaseTile

tile_repr ={'!': ActorTile,
            '#': WallTile,
            ' ': FloorTile}

class Position():
    def __init__(self, pos_x , pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return '({},{})'.format(self.pos_x, self.pos_y)


class Map():

    def __init__(self, source_file):
        self.source_file = source_file
        #self.size_x = None
        #self.size_y = None

        self.file_content = None
        self._prepare_map()
        print("Map loaded")
        self.print_map()

    def _prepare_map(self):

        try:
            with open(self.source_file) as f:
                file_content = f.readlines()
                #print(file_content)
            self.file_content = [x.strip('\n') for x in file_content]

        except (OSError, FileNotFoundError) as e:
            print("Can't find source file")
            raise e

        self.map = OrderedDict()
        x_index = 1
        for line in self.file_content:
            self.map[x_index] = {}
            y_index = 1
            for char in line:
                #print('processed char: {}'.format(repr(char)))
                tile = tile_repr.get(char, BaseTile)
                self.map[x_index][y_index] = tile(Position(x_index, y_index), char)
                y_index += 1
            x_index += 1

    def print_map(self):
        for row in self.map.keys():
            line = ''
            for col in self.map[row].keys():
                line += self.map[row][col].representation
            #print(line)

    def _get_tile_at_pos(self, pos):
        return self.map[pos.pos_x][pos.pos_y]

    def _set_tile_at_pos(self, tile, pos):
        self.map[pos.pos_x][pos.pos_y] = tile

    def do_move(self, src_pos, dst_pos):
        src_tile = self._get_tile_at_pos(src_pos)
        dst_tile = self._get_tile_at_pos(dst_pos)

        # logical change
        src_tile.set_pos(dst_pos)
        dst_tile.set_pos(src_pos)

        #map change
        self._set_tile_at_pos(src_tile, dst_pos)
        self._set_tile_at_pos(dst_tile, src_pos)
        ##return dst_pos


    def check_pos(self, pos):
        try:
            return (self._get_tile_at_pos(pos))
        except KeyError:
            return 'OutOfBounds'

    def try_move(self, src_pos, dst_pos):
        try:
            if self._get_tile_at_pos(src_pos).can_move \
                    and self._get_tile_at_pos(dst_pos).can_move_to:
                return True

            return False
        except KeyError:
            return 'OutOfBounds'

    def reload(self):
        self.map = self._prepare_map()



