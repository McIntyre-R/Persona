from miscFunc import pad, clear


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f'{self.name:^115}'
    def take(self):
        clear()
        pad()
        print(f"{f'You have taken {self.name}':^115}\n")
        pad()
        input(f"{f'Press [Enter] to continue':^115}")
        clear()

    def leave(self):
        clear()
        pad()
        print(f"{f'You leave {self.name} behind':^115}")
        pad()
        input(f"{f'Press [Enter] to continue':^115}")
        clear()
    
    
