# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,loc):
        self.name = name
        self.location = loc
        self.items = []
        self.hp = 100
    def move_rooms(self, room):
        self.location = room
    def take_item(self, item):
        self.items.append(item)
    def drop_item(self, item):
        self.items.remove(item)