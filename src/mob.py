from miscFunc import pad, clear

class Mob:
    def __init__(self, name, hp, element, strength, weakness, damage):
        self.name = name
        self.hp = hp
        self.element = element
        self.strength = strength
        self.weakness = weakness
        self.damage = damage
        self.scanned = False
    def take_damage(self, dmg):
        self.hp -= dmg
        clear()
        pad()
        print(f"{f'{self.name} takes {dmg} damage!':^115} \n")
        input(f"{'Press [enter] to continue':^115}")
    def deal_damage(self, player):
        if(player.element == self.strength):
            player.take_damage(self.damage*2)
        elif(player.element == self.weakness):
            player.take_damage(self.damage/2)
        else:
            player.take_damage(self.damage)
    
