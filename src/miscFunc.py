from os import system, name


def get_key(val, list): 
    for key, value in list.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def pad():
    print('\n \n \n \n \n')


def clear(): 
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 