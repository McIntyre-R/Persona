from miscFunc import clear, pad
from playsound import playsound



class Persona:
    def __init__(self, name, element, damage, spCost, strength, weakness, call, sound):
        self.name = name
        self.element = element
        self.damage = damage
        self.spCost = spCost
        self.strength = strength
        self.weakness = weakness
        self.call = call
        self.sound = sound

    def summon(self, player, mob):
        if(player.sp > self.spCost):
            player.use_sp(self.spCost)
            player.element = self.element
            playsound(self.sound)
            if(mob.element == self.strength):
                mob.take_damage(self.damage*2)
            elif(mob.element == self.weakness):
                mob.take_damage(self.damage/2)
            else:
                mob.take_damage(self.damage)
        else:
            clear()
            pad()
            print(f"{'Not enough sp to cast':^115} \n")
            input(f"{'Press [enter] to continue':^115}")