from utils import *
from slider import *
from select_coord import select_coord_on_pic

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy


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
        decrease_rate = 0.2
        k = (1/decrease_rate -1)/self.interest_thresh
        interest = 1/(k*popravka + 1)
        if popravka > self.interest_thresh:
            interest = 0
        return interest

    def count_statistics(self, pics_for_stat, n_bins):
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

    def get_reaction_on_pic(self, pic):
        res = np.full_like(pic, 0.0, dtype=np.float64)
        pic2 = np.pad(pic, self.side, mode='constant', constant_values=0)

        for coordy in range(0, res.shape[0]):
            for coordx in range(0, res.shape[1]):
                popravka, interest = self.apply(pic2, coordx + self.side-1, coordy + self.side-1)
                if interest is not None:
                    res[coordy, coordx] = interest
        return res

    def visualise_on_pic(self, pic):
        res = self.get_reaction_on_pic(pic)
        show_2_gray_pics(pic, res)


def create_descriptor_A():
    pic = handly_select_exemplars_of4()[0]
    xs,ys = select_coord_on_pic(pic)
    coordx = xs[0]
    coordy = ys[0]

    checker = check_mean
    side = 4

    A = DescriptorA(checker, side)
    A.apply_first_time(pic, coordx, coordy)
    pics_for_stat = get_diverse_set_of_numbers(10)
    A.count_statistics(pics_for_stat, 5)
    A.visualise_on_pic(pic)
    return A


if __name__ == "__main__":
    A = create_descriptor_A()
