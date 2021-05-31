import numpy as np


def get_sensory_array(pic, centerx, centery, side):
    xmin = centerx - int(side / 2)
    ymin = centery - int(side / 2)
    xmax = xmin +side
    ymax = ymin + side

    xlen = pic.shape[1]
    ylen = pic.shape[0]
    if xmin >=0 and ymin>=0 and xmax <xlen and ymax < ylen:
        return pic[ ymin:ymax, xmin:xmax]
    return None
#------------------CHECKERS-------------------------------------
def check_dispersion(pic, centerx, centery, side):
    sensory_array = get_sensory_array(pic, centerx, centery, side)
    if sensory_array is None:
        return None
    return np.var(sensory_array)

def check_mean(pic, centerx, centery, side):
    sensory_array = get_sensory_array(pic, centerx, centery, side)
    if sensory_array is None:
        return None
    return np.mean(sensory_array)

def check_perepad(pic, centerx, centery, side):
    sensory_array = get_sensory_array(pic, centerx, centery, side)
    if sensory_array is None:
        return None
    min = np.min(sensory_array)
    max = np.max(sensory_array)
    span = abs(max - min)
    return span

def check_energy(pic, centerx, centery, side):
    sensory_array = get_sensory_array(pic, centerx, centery, side)
    if sensory_array is None:
        return None
    checker = check_perepad
    side_sensory_array=2
    res = slide_no_pad(sensory_array, side_sensory_array, checker)
    return np.sum(res)


#---------------------------------------------------------------

def slide(pic, side, checker):

    res = np.full_like(pic, 0)
    for centery in range(0, pic.shape[0]):
        for centerx in range(0, pic.shape[1]):
            value = checker(pic, centerx, centery, side)
            if value is not None:
                res[centery, centerx] = value
    return res

def slide_no_pad(pic, side, checker):
    res = np.full_like(pic, 0)
    minpad = int(side/2)
    maxpad = side - minpad
    xmin =  minpad
    ymin =  minpad

    xmax = pic.shape[1] - maxpad
    ymax = pic.shape[0] - maxpad
    for centery in range(ymin, ymax+1):
        for centerx in range(xmin, xmax+1):
            value = checker(pic, centerx, centery, side)
            if value is not None:
                res[centery, centerx] = value
    return res









