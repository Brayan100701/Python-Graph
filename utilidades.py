import math

is_int = lambda num: isinstance(int(num), int)

def validate(min,max,inter):
    try:
        return is_int(min) and is_int(max) and is_int(inter)
    except:
        return False

def calc_val(num, func):
    match(func):
        case 'sin':
            return math.sin(num)
        case 'cos':
            return math.cos(num)
        case 'tan':
            return math.tan(num)
    

def calc_func(min, max, inter, func):
    x_axis = range(int(min),int(max),int(inter))
    y_axis = [calc_val(y,func) for y in x_axis]
    return x_axis, y_axis