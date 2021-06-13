from descriptorA import DescriptorA
from utils import *

import matplotlib.pyplot as plt
import numpy as np

class DescriptorUB:
    def __init__(self, descrB, ux, uy):
        self.ux = ux
        self.uy = uy
        self.descriptorB = descrB


    def get_all_hypotheses_in_point(self, pic, coordx, coordy):
        pic2 = self.descriptorB.get_reaction_on_pic(pic)

        centerx= coordx+self.ux
        centery= coordy+self.uy

        xlen = pic2.shape[1]
        ylen = pic2.shape[0]

        radius = 0

        radiuses = []
        best_activations = []

        while True:
            X, Y = get_coords_for_radius(radius, centerx, centery)
            counter=0
            for i in range(len(X)):
                x=X[i]
                y=Y[i]
                if x >= 0 and y >= 0 and x < xlen and y < ylen:
                    counter+=1
                    radiuses.append(radius)
                    best_activations.append(pic2[y, x])
            if counter==0:
                break
            else:
                radius=radius+1
        plt.scatter(radiuses, best_activations,alpha=0.3)

        plt.show()

if __name__ == "__main__":
    from descriptorA import create_descriptor_A
    from select_coord import *
    B = create_descriptor_A()
    uB= DescriptorUB(B, 0, 0)

    pic = handly_select_exemplars_of4()[0]
    xs, ys = select_coord_on_pic(pic)
    coordx = xs[0]
    coordy = ys[0]

    uB.get_all_hypotheses_in_point(pic, coordx, coordy)
