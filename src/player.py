# Write a class to hold player information, e.g. what room they are in
# currently.
from miscFunc import pad, clear
class Player:
    def __init__(self,name,loc):
        self.name = name
        self.location = loc
        self.objective = 'escape'
        self.items = ['Key']
        self.hp = 100
        self.sp = 100
        self.persona = ['Arsene',]
        self.element = 'none'
        self.damage = 5

    def move_rooms(self, room):
        self.location = room

    def take_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)

    def check_inventory(self):
        pad()
        print(f"{'You open your bag to find:':^115} \n")
        if len(self.items) == 0:
            print(f"{'The bag is empty.':^115} \n")
        elif len(self.items) <=3:
            for e in self.items:
                print(f'{e:^115}')
            print('\n')
        elif len(self.items) <=6:
            for e in self.items:
                print(e)

    def take_damage(self, dmg):
        self.hp -= dmg
        clear()
        pad()
        print(f"{f'{self.name} takes {dmg} damage!':^115} \n")
        input(f"{'Press [enter] to continue':^115}")

    def defense(self):
        heal = int(self.hp*.10)
        self.hp += heal
        if self.hp > 100:
            self.hp = 100
        clear()
        pad()
        print(f"{f'{self.name} heals {heal} hit points!':^115} \n")
        input(f"{'Press [enter] to continue':^115}")
        
    def use_sp(self, cost):
        self.sp -= cost

    def scan_enemy(self, mob):
        mob.scanned = True
        self.use_sp(20)
        clear()
        pad()
        print(f"{f'{self.name} scans {mob.name} revealing its element!':^115} \n")
        input(f"{'Press [enter] to continue':^115}")


    
        
