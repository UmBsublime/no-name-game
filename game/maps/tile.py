

class BaseTile:

    def __init__(self, position, representation):
        self.type = 'BaseTile'
        self.position = position
        self.representation = representation

    def get_pos(self):
        return self.position

    def set_pos(self, new_pos):
        self.position = new_pos

    def __str__(self):
        return self.__class__.__name__


class ActorTile(BaseTile):
    can_move = True
    can_move_to = False
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.type = 'ActorTile'


class DecorTile(BaseTile):
    can_move = False
    can_move_to = False
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WallTile(DecorTile):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FloorTile(DecorTile):
    can_move_to = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

