from utils import *
from slider import *
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    pics = get_numbers_of_type(the_number=3)
    print(pics.shape)
    side = 3
    pic = pics[0]
    pic = np.pad(pic, side, mode='constant', constant_values=0)

    checker = check_energy
    pic2 = slide(pic, side, checker)
    show_2_gray_pics(pic, pic2)
