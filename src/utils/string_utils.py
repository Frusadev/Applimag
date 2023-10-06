def file_name(preffix:str, extension:str):
    return preffix + '.' + extension

def non_null_input(message:str) -> str:
    inp = input(message)
    while inp.isspace():
        inp = input(message)
    return inp

def starts_with_any_value_in(string:str, values:list[str]) -> bool:
    for vals in values:
        if string.startswith(vals):
            return string.startswith(vals)
    return False


"""This function take 4 parameters: 
The message,
the firt_string and the second_string that are going to be compared to each other
and low: which determines whether the comparison is an equivalence or not
"""
def either(message: str, first_string: str, second_string: str, low: bool) -> bool:
    res = input(message)
    if low:
        while res.lower() != first_string.lower() and res.lower() != second_string.lower():
            res = input(message)
        return res.lower() == first_string.lower()
    else:
        while res != first_string and res != second_string:
            res = input(message)
        return res == first_string


"""
It compares a value to a list of values and returns the one selected
if low:
We'll iterate through the set, we'll compare every value and if one match then we'll return it 
ohterwise the returned value will be none (lower)

(case)
We'll iterate through the set, we'll compare every value and if one match then we'll return it 
ohterwise the returned value will be none
"""
def any_of(message:str, values:set[str], low:bool) -> str:
    res = input(message)
    if low:
        values_lowered = {vals.lower() for vals in values}
        while not res.lower() in values_lowered:
            res = input(message)
        return res
    else:
        while not res.lower() in values:
            res = input(message)
        return res

def color(text:str, color:str):
    red = '\033[31m'
    black = '\033[30m'
    white = '\033[37m'
    green = '\033[32m'
    yellow = '\033[33m'
    orange = '\033[91m'
    blue = '\033[34m'
    brown = '\033[38;5;130m'
    no_color = '\033[0m'

    colors = {'red': red, 'black': black, 
     'white': white, 'green': green,
     'yellow': yellow, 'orange': orange,
     'blue': blue, 'brown': brown, 'none': no_color}

    
    c = {col:colors[col] for col in colors if color.lower() == col}
    
    if not c.__len__() == 0:
        return c[color] + text + no_color
    return no_color + text + no_color

def input_starts_with(message:str, preffix:str, low=False):
    inp = input(message)
    if low:
        while not inp.lower().startswith(preffix.lower):
            inp = input(message)
        return inp
    while not inp.startswith(preffix):
        inp = input(message)
    return inp

def cut(text:str, size:int, suffix:str) -> str:
    cursor = 0
    output = ''
    for char in text:
        if cursor < size:
            output.__add__(char)
            cursor += 1
        else: break
    output.__add__(suffix)
    return output