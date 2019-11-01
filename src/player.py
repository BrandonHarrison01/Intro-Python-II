# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        self.room = room
        self.bag = []

    def __str__(self):
        return f"{self.room}"

    def add_item(self, item):
        self.bag.append(item)

    def drop_item(self, item):
        self.bag.append(item)
