# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loot = []

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        room = f'{self.name}, {self.desc}.'

        l = ''

        for i in self.loot:
            l += f'{i.name} '

        return room + '\n' + 'Loot: ' + l

    def add_item(self, item):
        self.loot.append(item)

    def drop_item(self, item):
        self.loot.append(item)
