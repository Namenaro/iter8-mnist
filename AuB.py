from descriptorA import *
import numpy as np
import matplotlib.pyplot as plt

def get_random_coord(side):
    xy = np.random.randint(side, size=2)
    x=xy[0]
    y=xy[1]
    return x, y

def get_random_pic_index(num_pics):
    pic_id = np.random.randint(num_pics)
    return pic_id

def find_all_above_threshold_around_coord(descr, pic, centerx, centery):
    pic2 = descr.get_reaction_on_pic(pic)
    X = []
    Y = []
    for coordy in range(0, pic2.shape[0]):
        for coordx in range(0, pic2.shape[1]):
            if pic2[coordy,coordx] > 0:
                X.append(coordx-centerx)
                Y.append(coordy-centery)
    return X, Y

def visualise_2d_hist(X,Y):
    plt.hist2d(X, Y, bins=(14, 14), density=True, cmap=plt.cm.Reds)
    plt.clim(0, 0.002)
    plt.colorbar()
    plt.show()

def calculate_stat_of_descriptor(pics, descr):
    side = pics[0].shape[0]
    num_pics = len(pics)
    n_experiments = 1000
    allX = []
    allY = []
    for _ in range(n_experiments):
        pic_id = get_random_pic_index(num_pics)
        pic = pics[pic_id]
        x, y = get_random_coord(side)
        X, Y = find_all_above_threshold_around_coord(descr, pic, x, y)
        allX=allX+X
        allY=allY+Y
    visualise_2d_hist(allX, allY)

if __name__ == "__main__":
    A = create_descriptor_A()
    pics = get_diverse_set_of_numbers(n=100)
    calculate_stat_of_descriptor(pics, A)