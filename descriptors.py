from utils import *
from slider import *
from select_coord import select_coord_on_pic

import numpy as np
import matplotlib.pyplot as plt


class DescriptorA:
    def __init__(self, checker, side):
        self.checker = checker
        self.side = side
        self.etalon_val = None
        self.statistics = None

    def apply_first_time(self, pic, coordx, coordy):
        val = self.checker(pic, coordx, coordy, self.side)
        if val is None:
            print("bad coordinate for checker")
        self.etalon_val = val

    def apply(self, pic, coordx, coordy):
        val = self.checker(pic, coordx, coordy, self.side)
        if val is None:
            return None, None
        interest = self.count_interest(val)
        return val, interest

    def count_interest(self, value):
        interest = 0
        return interest

    def count_statistics(self, pics_for_stat):
        pass

def create_descriptor_A():
    pic = handly_select_exemplars_of4()[0]
    xs,ys = select_coord_on_pic(pic)
    coordx = xs[0]
    coordy = ys[0]

    checker = check_mean
    side = 4

    A = DescriptorA(checker, side)
    A.apply_first_time(pic, coordx, coordy)
    pics_for_stat = get_diverse_set_of_numbers(100)
    A.count_statistics(pics_for_stat)
    return A


if __name__ == "__main__":
    A = create_descriptor_A()
