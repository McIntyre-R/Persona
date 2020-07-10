




def cell_event(player, room):
    choice = ''
    while room.event == True and player.hp > 0 and not choice == 'q':
        input('test')
        room.event = False