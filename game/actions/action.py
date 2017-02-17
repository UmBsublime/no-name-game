class ActionResult():
    SUCCESS = True
    FAILURE = False

    def __init__(self, result, alternative):
        self.succeded = result
        self._alternative = alternative

    @property
    def alternative(self):
        if self.succeded:
            return None
        else:
            return self._alternative


class BaseAction():

    def __init__(self):
        pass

    def perform(self):
        raise NotImplemented


class Walk(BaseAction):

    def __init__(self, direction):
        self.direction = direction
        super().__init__()

    def perform(self):
        return ActionResult(True)
