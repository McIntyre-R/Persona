from miscFunc import pad, clear


class Item:
    def __init__(self, name, description):
        self.name: name
        self.description: description
    def take(self):
        clear()
        print(f"{f'You have taken {self.name}':^115}")
        pad()
        input(f"{f'Press [Enter] to continue':^115}")
        clear()

    def leave(self):
        clear()
        print(f"{f'You leave {self.name} behind':^115}")
        pad()
        input(f"{f'Press [Enter] to continue':^115}")
        clear()
    
