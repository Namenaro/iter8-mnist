from utils import *
from slider import *
from select_coord import select_coord_on_pic

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy
from kneed import KneeLocator

class DescriptorA:
    def __init__(self, checker, side):
        self.checker = checker
        self.side = side
        self.etalon_val = None
        self.interest_thresh = None
        self.informativness_of_descriptor = None

    def apply_first_time(self, pic, coordx, coordy):
        val = self.checker(pic, coordx, coordy, self.side)
        if val is None:
            print("bad coordinate for checker")
        self.etalon_val = val

    def apply(self, pic, coordx, coordy):
        val = self.checker(pic, coordx, coordy, self.side)
        if val is None:
            return None, None
        popravka = abs(self.etalon_val - val)
        interest = self.count_interest(popravka)
        return popravka, interest

    def count_interest(self, popravka):
        b = 0.2
        k = (1/b -1)/self.interest_thresh
        interest = 1/(k*popravka + 1)
        return interest

    def count_statistics(self, pics_for_stat,n_bins):
        popravs = np.array([])
        for pic in pics_for_stat:
            activations_on_pic = slide(pic, self.side, self.checker).flatten()
            popravs_on_pic = np.absolute(activations_on_pic-self.etalon_val)
            popravs = np.concatenate([popravs, popravs_on_pic])
        (probs, bins, _) = plt.hist(popravs, bins=n_bins, weights=np.ones_like(popravs) / len(popravs), range=(0,popravs.max()))
        plt.show()
        i = np.argmax(probs)
        self.interest_thresh = bins[i]
        self.informativness_of_descriptor = i/(n_bins-1)

        print("informativness = " + str(self.informativness_of_descriptor))
        print("interest_thresh = " + str(self.interest_thresh))





def create_descriptor_A():
    pic = handly_select_exemplars_of4()[0]
    xs,ys = select_coord_on_pic(pic)
    coordx = xs[0]
    coordy = ys[0]

    checker = check_mean
    side = 5

    A = DescriptorA(checker, side)
    A.apply_first_time(pic, coordx, coordy)
    pics_for_stat = get_diverse_set_of_numbers(10)
    A.count_statistics(pics_for_stat, 5)
    return A


if __name__ == "__main__":
    A = create_descriptor_A()
