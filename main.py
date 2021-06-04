from utils import *
from slider import *
from select_coord import select_coord_on_pic

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    #pics = get_numbers_of_type(the_number=2)
    #print(pics.shape)
    side = 5
    checker = check_dispersion
    #pic = pics[6]
    #pic = np.pad(pic, side, mode='constant', constant_values=0)

    #pic2 = slide(pic, side, checker)
    #show_2_gray_pics(pic, pic2)

    pics = get_numbers_of_type(the_number=9)[0:90]
    #get_stat(pics, side, checker)
    x,y = select_coord_on_pic(pics[0])
    print(x)