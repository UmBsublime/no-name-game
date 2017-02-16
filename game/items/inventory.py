class BaseInventory():

    def __init__(self, size, content=[]):
        self.size = size
        self.content = content

    def get_item(self):
        pass

    def get_content(self):
        pass

    def show_content(self):
        for item in self.content:
            print(' - ' + item.name)
            if item.__str__() == 'Disposable':
                for effect in item.effects:
                    print('   - {}: {}'.format(effect.name, effect.effect_value))
            if item.__str__() == 'Weapon':
                print('   - Dmg: {}'.format(item.dmg))

    def add_item(self):
        pass

    def remove_item(self):
        pass
