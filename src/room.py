# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f'    You find yourself at the {self.name}. \n    {self.description}.'

    def check_room(self):
        if len(self.items) == 0:
            print("The room is empty.")
        elif len(self.items) <=3:
            for e in self.items:
                print(f'{e:^115}')
        elif len(self.items) <=6:
            for e in self.items:
                print(e)

    def leave_item(self, item):
        self.items.append(item)
    
    def take_item(self, item):
        self.items.remove(item)