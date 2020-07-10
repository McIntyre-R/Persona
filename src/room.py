# Implement a class to hold room information. This should have name and
# description attributes.
from miscFunc import pad
class Room:
    def __init__(self,name,description, items, key, event):
        self.name = name
        self.description = description
        self.items = items
        self.key = key
        self.event = event #bool

    def __str__(self):
        return f'    You find yourself at the {self.name}.'

    def check_room(self):
        pad()
        print(f"{'You scan the room to find:':^115} \n")
        if len(self.items) == 0:
            print(f"{'The room is empty.':^115} \n")
        elif len(self.items) <=3:
            for e in self.items:
                print(f'{e:^115}')
            print('\n')
        elif len(self.items) <=6:
            for e in self.items:
                print(e)

    def drop_item(self, item):
        self.items.append(item)
    
    def take_item(self, item):
        self.items.remove(item)

    

    