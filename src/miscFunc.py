from os import system, name


def get_key(val, list): 
    for key, value in list.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def pad(num = 4):
    print('\n'*num)


def clear(): 
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 


def text(text, lineBreaks):
    print(f"{f'{text}':^115}",  lineBreaks)


def get_persona(dict):
    p_options = []
    for e in dict.keys():
        char = e[0].lower()
        string = f"[{char}] {e}"
        p_options.append(string)
    return p_options
