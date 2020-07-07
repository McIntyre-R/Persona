from room import Room
from player import Player
from moves import Moves
import winsound, time, random
from playsound import playsound
from miscFunc import pad, get_key, clear


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# item = {
#     'key': Item()
# }
# print(random.randint(0,10))

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
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

playsound('cantBe.wav')
time.sleep(1)
playsound('notHere.wav')
time.sleep(1)
playsound('stillFight.wav')
time.sleep(1)

winsound.PlaySound("Aria.wav",  winsound.SND_ASYNC)
pad()
time.sleep(4)
for e in intro1:
    print(e)
    time.sleep(3)
name = input("Enter your name:")
player = Player( name , 'outside')

intro2 = [f"{f'Very well then...':^115}\n",
f"{f'I shall lend you my strength... {player.name}':^115}\n"]

time.sleep(3)
for e in intro2:
    print(e)
    time.sleep(3)
clear()

pad()
for e in title:
    print(f'{e:^116}')
    time.sleep(0.5)
time.sleep(3)
input(f"{'Press [Enter] to start...':^115}")

playsound('start.wav')
time.sleep(0.5)
winsound.PlaySound(None,  winsound.SND_ASYNC)
clear()
time.sleep(2)
winsound.PlaySound('villain.wav', winsound.SND_ASYNC)
time.sleep(2)
pad()
for e in prolouge:
    print(e)
    time.sleep(3)
input(f'{"Press [enter] to continue...":>230}')
clear()
pad()
for e in arsene1:
    print(e)
    time.sleep(3)
reply = input(f'{" Reply: [q] It wasnt [w] It Might have been...":>230}\n')
clear()
pad()
if reply == 'w':
    print(f'{"No need for mere words. Show me your true feelings.":^115}\n')
    time.sleep(3)
for e in arsene2:
    print(e)
    time.sleep(3)
input(f'{"Reply: [q] THATS ENOUGH [w] I WILL STOP YOU":>230}\n')
clear()
winsound.PlaySound('WillPower.wav',  winsound.SND_ASYNC)
playsound('persona3.wav')
time.sleep(4)


while not choice == 'q' and player.hp > 0:
    pad()
    print(room[player.location], '\n')
    pad()
    print(f'    {player.name}\n    HP: {player.hp}/100')
    choice = input(f"{'[m] move, [q] quit':>230} \n" )

    clear()
    pad()
    print(room[player.location], '\n')
    if choice == '':
            clear()
            pad()
            print(f'{"Dont just press enter dummy, try again":^115}')
            time.sleep(2)
            clear()
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
                if moves[m].dest == '':
                    pad()
                    print(f'{"thats a wall dummy, try again":^115}')
                    time.sleep(2)
                    clear()
                else:
                    player.move_rooms(moves[m].dest)
            

winsound.PlaySound('gameOver.wav', winsound.SND_ASYNC)
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