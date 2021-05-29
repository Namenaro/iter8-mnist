from utils import *

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    pics = get_numbers_of_type(the_number=3)
    print(pics.shape)
    show_2_gray_pics(pics[0], pics[1])