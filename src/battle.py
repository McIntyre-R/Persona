
from miscFunc import clear, pad, get_persona
from playsound import playsound
import random
import winsound


battleSound = ['assets/voice/takeThis.wav', 'assets/voice/itsOver.wav', 'assets/voice/gotYou.wav', 'assets/voice/die.wav', 'assets/voice/fall.wav', 'assets/voice/giveItUp.wav', 'assets/voice/gotEm.wav']
victorySound = ['assets/voice/Alright.wav','assets/voice/Okay.wav','assets/voice/powerCourse.wav','assets/voice/stepForward.wav']
hitSound = ['assets/sounds/bash.wav','assets/sounds/hit.wav','assets/sounds/slash.wav','assets/sounds/stab.wav']
def Battle(enemy, player, personas):
    choice = ''

    while enemy.hp > 0 and player.hp > 0:
        clear()
        pad()
        print(f"{f'{enemy.name}':^115} \n")
        print(f"{f'{enemy.hp}/100 HP':^115} \n")
        if enemy.scanned == True:
            print(f"{f'Element: {enemy.element}':^115}")
        pad()
        print(f'    {player.name}\n    HP: {player.hp}/100\n    SP: {player.sp}/100\n Current Element: {player.element}')
        if enemy.scanned == True:
            choice = input(f"{'[a] attack, [p] summon persona, [d] defend':>230} \n" )
        else:
            choice = input(f"{'[a] attack, [p] summon persona, [d] defend, [s] scan (20sp)':>230} \n" )
        if choice == 'a':
            playsound(random.choice(battleSound))
            playsound(random.choice(hitSound))
            enemy.take_damage(player.damage)
        if choice == 'p':
            clear()
            pad()
            print(f"{f'{enemy.name}: {enemy.hp} HP':^115} \n")
            pad()
            print(f'    {player.name}\n    HP: {player.hp}/100')
            persona_options = [""]
            for e in get_persona(personas):
                persona_options.insert(0,e)
            persona_string = ','
            persona_string = persona_string.join(persona_options)
            choice = input(f"{f'{persona_string}':>230}\n")
            for e in personas.keys():
                char = e[0].lower()
                if choice == char:
                    playsound(personas[e].call)
                    personas[e].summon(player,enemy)
                    
        if choice == 'd':
            playsound('assets/sounds/defUp.wav')
            player.defense()
            enemy.deal_damage(player)
        if choice == 's':
            player.scan_enemy(enemy)
    

    winsound.PlaySound('assets/songs/victory.wav',winsound.SND_ASYNC)
    playsound(random.choice(victorySound))
    clear()
    pad()
    print(f"{f'{enemy.name} has been vanquished':^115} \n")
    if random.randint(0,10) == 1:
        player.items.append('Health Potion')
        print(f"{f'{enemy.name} dropped a health potion!':^115} \n")
    input(f"{'Press [enter] to continue...':>230}")