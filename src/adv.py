from room import Room
from player import Player
from moves import Moves
import winsound, time, random
from playsound import playsound
from miscFunc import pad, get_key, clear, get_persona
from item import Item
from mob import Mob
from persona import Persona
from battle import Battle
from cell_event import cell_event


# Declare all the rooms

room = {
    'cell':  Room("Dungeon Cell",
                     "Blood stains the floor from all the people Kamoshida has tortured. To the north is a cell door left ajar as Kamoshida ran away. ",
                     ["Gun", 'Sword', 'Match'],
                     "Key",
                     True),

    'foyer':    Room("Foyer",
                     " Dim light filters in from the south. Dusty passages run north and east.",
                     [], "", True),

    'overlook': Room("Grand Overlook", 
                     " A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", 
                     [], "", True),

    'narrow':   Room("Narrow Passage",
                     " The narrow passage bends here from west to north. The smell of gold permeates the air.",
                     [], "", True),

    'treasure': Room("Treasure Chamber",
                     " You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
                     [], "", True),
}

item = {
    'Gun': Item('Gun', 'Big Gun'),
    'Sword': Item('Sword', 'Single Sword'),
    'Match': Item('Match', 'Match'),
    'Key': Item('Key', 'temp')
}

enemy = {
    'Guard': [ 'Guard', 50, 'Earth', 'none', 'none', 1],
}

persona = {
    'Arsene': Persona( 'Arsene', 'Fire', 10, 20, 'Earth', 'Water', 'assets/voice/Arsene.wav', 'assets/sounds/ArSkill.wav')
}


battleSound = ['assets/voice/takeThis.wav', 'assets/voice/itsOver.wav', 'assets/voice/gotYou.wav', 'assets/voice/die.wav', 'assets/voice/fall.wav', 'assets/voice/giveItUp.wav', 'assets/voice/gotEm.wav']
battleStart = ['assets/sounds/battle1.wav','assets/sounds/battle2.wav','assets/sounds/battle3.wav']
hitSound = ['assets/sounds/bash.wav','assets/sounds/hit.wav','assets/sounds/slash.wav','assets/sounds/stab.wav']

# print()
random_mob = random.choice(list(enemy.keys()))
random_enemy = Mob(*enemy[random_mob])
# Link rooms together

room['cell'].n_to = room['foyer']
room['foyer'].s_to = room['cell']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

title = ['8b,dPPYba,   ,adPPYba, 8b,dPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba,  ,adPPYYba, ',
'88P\'    \"8a a8P_____88 88P\'   \"Y8 I8[    \"\" a8\"     \"8a 88P\'   `\"8a \"\"     `Y8  ',
'88       d8 8PP\"\"\"\"\"\"\" 88          `\"Y8ba,  8b       d8 88       88 ,adPPPPP88  ',
'88b,   ,a8" "8b,   ,aa 88         aa    ]8I "8a,   ,a8" 88       88 88,    ,88  ',
'88`YbbdP\"\'   `\"Ybbd8\"\' 88         `\"YbbdP\"\'  `\"YbbdP\"\'  88       88 `\"8bbdP\"Y8  ',
'88                                                                              ',
'88                                                                          \n\n\n\n'
]

choice = ''

intro1 = [f"{'I am thou... ':^115}\n",
f"{'Thou art I... ':^115}\n", 
f"{'From the sea of thy soul, I come... ':^115}\n"]


prolouge = [f"{'...Hmph. Whered your energy from earlier go?':^115}",
f"{'A peasant like you isnt worth beating':^115}",
f"{'Ill have you killed right now':^115}\n\n\n",
f"{'Before you stands Kamoshida, the king of this realm.':^115}",
f"{'You cant remember how you got here, but in trying to escape you were caught.':^115}",
f"{'Now too weak to move... all you can do is await the end...':^115}\n\n",
f"{'However as you lay there motionless, a voice echos in your head as it did moments earlier...':^115}\n"
]

arsene1 = [
    f"{'Whats the matter...? Are you simply going to watch?':^115}",
    f"{'Have you already forsaken yourself?':^115}",
    f"{'Death awaits you if you do not act.':^115}",
    f"{'Was your previous decision a mistake then?':^115} \n\n"
]

arsene2 = [
    f"{'Very well... I have heeded your resolve.':^115}",
    f"{'Vow to me.':^115}",
    f"{'I am thou, thou art I...':^115}",
    f"{'Thou who art willing to perform all sacrilegious acts for thine own justice!':^115}",
    f"{'Call upon my name, and release thy rage!':^115}",
    f"{'Show the strength of thy will to ascertain all on thine own, though thou be chained to Hell itself!':^115}\n\n\n",
    f"{'Kamoshida: Execute Him!':^115}\n\n"
]

arsene3 = [
    f"{'With those words a demon emerges from behind you...':^115}",
    f"{'As if a shadow made manifest the figure continues to grow behind you,':^115}",
    f"{'Now towering above you the figure speaks a familiar voice...':^115}\n\n",
    f"{'I am the pillager of twilight-- Arsene!':^115}\n",
    f"{'I am the rebels soul that resides within you.':^115}\n"
    f"{'If you so desire, I shall consider granting you the power to break through this crisis.':^115}\n"
]

arsene4 = [
    f"{'Arsene: Hmph, very well...':^115} \n\n",
    f"{'Kamoshida: Who the hell are you...!?':^115}",
    f"{'Guards!':^115}",
    f"{'Start by killing that one!':^115}",
    f"{'Youll learn the true strength of my men!':^115}\n"
]


    # f"{'':^115}"


# playsound('assets/voice/cantBe.wav')
# time.sleep(1)
# playsound('assets/voice/notHere.wav')
# time.sleep(1)
# playsound('assets/voice/stillFight.wav')
# time.sleep(1)

# winsound.PlaySound("assets/songs/Aria.wav",  winsound.SND_ASYNC)
# pad()
# time.sleep(4)
# for e in intro1:
#     print(e)
#     time.sleep(3)
name = input("Enter your name:")
player = Player( name , 'cell')

# intro2 = [f"{f'Very well then...':^115}\n",
# f"{f'I shall lend you my strength... {player.name}':^115}\n"]

# time.sleep(3)
# for e in intro2:
#     print(e)
#     time.sleep(3)
# clear()

# pad()
# for e in title:
#     print(f'{e:^116}')
#     time.sleep(0.5)
# time.sleep(2)
# input(f"{'Press [Enter] to start...':^115}")

# playsound('assets/sounds/start.wav')
# time.sleep(0.3)
# winsound.PlaySound(None,  winsound.SND_ASYNC)
# clear()
# time.sleep(2)
# winsound.PlaySound('assets/songs/villain.wav', winsound.SND_ASYNC)
# time.sleep(2)
# pad()
# for e in prolouge:
#     print(e)
#     time.sleep(3)
# input(f'{"Press [enter] to continue...":>230}')
# clear()
# pad()
# for e in arsene1:
#     print(e)
#     time.sleep(3)
# reply = input(f'{" Reply: [q] It wasnt [w] It Might have been...":>230}\n')
# clear()
# pad()
# if reply == 'w':
#     print(f'{"No need for mere words. Show me your true feelings.":^115}\n')
#     time.sleep(3)
# for e in arsene2:
#     print(e)
#     time.sleep(3)
# input(f'{"Reply: [q] THATS ENOUGH [w] I WILL STOP YOU":>230}\n')
# clear()
# pad()
# winsound.PlaySound('assets/songs/WillPower.wav',  winsound.SND_ASYNC)
# playsound('assets/voice/persona3.wav')
# for e in arsene3:
#     print(e)
#     time.sleep(3)
# input(f"{'Reply: [q] Give me your power. [w] I dont want to die.':>230}\n")
# clear()
# pad()
# for e in arsene4:
#     print(e)
#     time.sleep(3)
# input(f"{'Press [enter] to continue...':>230}\n")
# clear()
# pad()
# tut_enemy = Mob(*enemy['Guard'])
# print(f"{'Arsene: Detest the enemies before you! Change that animosity into power... and unleash it!':^115}\n")
# time.sleep(3)
# print(f"{'Swing your blade!':^115}\n\n\n")
# time.sleep(3)
# print(f"{'During Battles you will fight until you or the enemies hp reach 0':^115}")
# time.sleep(3)
# print(f"{'Input [a] to perform a basic attack, try it now... ':^115}\n")
# time.sleep(3)
# print(f"{f'{tut_enemy.name}: {tut_enemy.hp} HP':^115} \n")
# pad()
# print(f'    {player.name}\n    HP: {player.hp}/100\n    SP: {player.sp}/100\n Current Element: {player.element}')
# choice = input(f"{'[a] attack':>230} \n" )
# playsound(random.choice(battleSound))
# playsound(random.choice(hitSound))
# tut_enemy.take_damage(player.damage)
# clear()
# pad()
# print(f"{'Arsene: This power of mine is yours!':^115}\n\n\n")
# time.sleep(3)
# print(f"{'As you progress through the game you will garner the favor of powerful demons':^115}")
# time.sleep(3)
# print(f"{'These demons other wise known as Personas can be summoned to perform powerful spells':^115}")
# time.sleep(3)
# print(f"{'However these spells cost SP(Spirit Points), and cannot be summoned without it.':^115}")
# time.sleep(3)
# print(f"{'Try summoning Arsene now from your persona menu...':^115}\n")
# time.sleep(3)
# print(f"{f'{tut_enemy.name}: {tut_enemy.hp} HP':^115} \n")
# pad()
# print(f'    {player.name}\n    HP: {player.hp}/100\n    SP: {player.sp}/100\n Current Element: {player.element}')
# choice = input(f"{'Input [p] to open your persona menu... ':>230} \n" )
# choice = input(f"{'Now choose Arsene by inputing: [a] Arsene... ':>230}\n")
# persona['Arsene'].summon(player,tut_enemy)
# clear()
# pad()
# time.sleep(3)
# print(f"{'Arsene: Kill them however you want. Run wild to your hearts content!':^115}\n\n\n")
# time.sleep(3)
# print(f"{'All enemies have an Elemental Association. These fall into one of three types:':^115}")
# time.sleep(3)
# print(f"{' Fire -- Earth -- Water ':^115}")
# time.sleep(3)
# print(f"{'Elements are strong to the element that comes after it (i.e Water is strong against Fire)':^115}")
# time.sleep(3)
# print(f"{'Conversly all elements are weak to the element before it (i.e Fire is weak against Water)':^115}")
# time.sleep(3)
# print(f"{'Every time you use a persona your element will be changed to that of the persona you used':^115}")
# time.sleep(3)
# print(f"{'Careful use of this system to exploit Enemy Weakness, and protect against Enemy Strength will prove vital':^115}\n")
# time.sleep(3)
# input(f"{'Press [enter] to continue...':>230}")
# Battle(tut_enemy, player, persona)

        

while not choice == 'q' and player.hp > 0:
    enc_num = random.randint(1,10)
    if player.sp <= 95:
        player.sp += 5

    if room[player.location].event == True and room[player.location].key in player.items:
        cell_event(player, room[player.location])

    elif enc_num <= 4 and not choice == 'r':
        playsound(random.choice(battleStart))
        winsound.PlaySound('assets/songs/TakeOver.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        random_mob = random.choice(list(enemy.keys()))
        
        random_enemy = Mob(*enemy[random_mob])
        Battle(random_enemy, player, persona)
    clear()
    pad()
    winsound.PlaySound('assets/songs/KingLoop.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
    print(f'{room[player.location]} \n')
    desc = room[player.location].description.split('.')
    for e in desc:
        print(f'   {e}')
    pad()
    print(f'    {player.name}\n    HP: {player.hp}/100\n    SP: {player.sp}/100\n Current Element: {player.element}')
    choice = input(f"{'[i] inventory, [e] explore room, [m] move, [q] quit':>230} \n" )
    clear()
    pad()
    print(room[player.location], '\n')
    if choice == '':
        clear()
        pad()
        print(f'{"Dont just press enter dummy, try again":^115}')
        time.sleep(2)
        clear()   
    if choice == 'e':
        while not choice == 'r':
            clear()
            room[player.location].check_room()
            choice = input(f"{'[<item>] Take Item,[R] Return ':>230} \n")
            clear()
            if(choice in room[player.location].items):
                pad()
                item[choice].take()
                player.take_item(choice)
                room[player.location].take_item(choice)
    if choice == 'i':
        while not choice == 'r':
            clear()
            player.check_inventory()
            choice = input(f"{'[<item>] Drop Item,[R] Return ':>230} \n")
            clear()
            pad()
            if choice in player.items:
                if choice.lower() == 'health potion':
                    player.hp += 10
                    player.items.remove('Health Potion')
                    print(f"{'You consume the health potion, gaining 10hp':^115}")
                    input(f"{'Press [enter] to continue...':>230}")
                else:
                    item[choice].leave()
                    player.drop_item(choice)
                    room[player.location].drop_item(choice)

    if choice == 'm':
        move_options = ["['q'] quit"]
        moves = {
            'north': Moves('n',''),
            'east': Moves('e',''),
            'west': Moves('w',''),
            'south': Moves('s','')
        }
        for e in dir(room[player.location]):
            if e == 'n_to':
                moves['north'].dest = get_key(room[player.location].n_to, room)
                move_options.insert(0,f"['n'] {room[player.location].n_to.name} ")
            if e == 'e_to':
                moves['east'].dest = get_key(room[player.location].e_to, room)
                move_options.insert(0,f"['e'] {room[player.location].e_to.name} ")
            if e == 's_to':
                moves['south'].dest = get_key(room[player.location].s_to, room)
                move_options.insert(0,f"['s'] {room[player.location].s_to.name} ")
            if e == 'w_to':
                moves['west'].dest = get_key(room[player.location].w_to, room)
                move_options.insert(0,f"['w'] {room[player.location].w_to.name} ")
        move_string = ','
        move_string = move_string.join(move_options)
        choice = input(f"{f'{move_string}':>230} \n")
        if choice == '':
                clear()
                pad()
                print(f'{"Dont just press enter dummy, try again":^115}')
                time.sleep(2)
                clear()
        for m in moves:
            if moves[m].key == choice:
                clear()
                winsound.PlaySound(None, winsound.SND_ASYNC)
                playsound('assets/sounds/move.wav')
                if moves[m].dest == '':
                    pad()
                    print(f'{"thats a wall dummy, try again":^115}')
                    time.sleep(2)
                    clear()
                else:
                    player.move_rooms(moves[m].dest)


if player.hp <= 0:
    winsound.PlaySound('assets/gameOver.wav', winsound.SND_ASYNC)
    clear()
    pad()
    print(f"{'Thou hast fallen and lost thy noble life. ':^115}\n")
    time.sleep(4)
    print(f"{'The hero hath crumbled over the weight':^115}")
    print(f"{'of his own justice.  His story of revolution':^115}")
    print(f"{'reacheth not the ears of the people.':^115}\n")
    time.sleep(4)
    print(f"{'The torch of courage that hath begun to kindle':^115}")
    print(f"{'hath now been extinguished by tainted winds...':^115}")
    time.sleep(6)
    clear()
    pad()
    print(f"{'Bad End':^115}")
    time.sleep(4)