import numpy as np
import matplotlib.pyplot as plt
import torchvision.datasets as datasets

def get_train_mnist():
    mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
    return mnist_trainset

def draw_several(np_images, np_labels, rows = 5, cols = 7):
    num_of_images = rows*cols
    for index in range(1, num_of_images + 1):
        plt.subplot(rows, cols, index)
        plt.axis('off')
        if np_labels is not None:
            plt.title(np_labels[index-1])
        plt.imshow(np_images[index-1].squeeze(), cmap='gray_r')
    plt.show()

def get_exact_numbers(the_number, np_images, np_labels):
    results = []

    for i in range(len(np_labels)):
        if np_labels[i] == the_number:
            results.append(np_images[i])
    return np.array(results)


def get_numbers_of_type(the_number):
    mnist_train = get_train_mnist()
    np_images = mnist_train.train_data.numpy()
    np_labels = mnist_train.train_labels.numpy()
    return get_exact_numbers(the_number, np_images, np_labels)

def show_2_gray_pics(pic1, pic2):
    fig = plt.figure()
    plt.gray()  # show the filtered result in grayscale
    ax1 = fig.add_subplot(121)  # left side
    ax2 = fig.add_subplot(122)  # right side
    ax1.imshow(pic1)
    ax2.imshow(pic2)
    plt.show()

def show_parad_of_the_number(the_number):
    np_images = get_numbers_of_type(the_number)
    np_labels = list(range(0, len(np_images)-1))
    i=0
    while True:
        draw_several(np_images[i:i+35], np_labels[i:i+35], rows= 5, cols=7)
        i=i+35

def handly_select_exemplars_of3():
    np_images = get_numbers_of_type(the_number=3)
    indexes = [34,32,25,67,68,35,210,314,420, 496,620,659,635,667,733,715]
    exemplars = list([np_images[ind] for ind in indexes])
    draw_several(exemplars, indexes, rows=2, cols=int(len(indexes)/2))
    return exemplars

def handly_select_exemplars_of1():
    np_images = get_numbers_of_type(the_number=1)
    indexes = [0,7,28,18,27,41,76,98]
    exemplars = list([np_images[ind] for ind in indexes])
    draw_several(exemplars, indexes, rows=2, cols=int(len(indexes) / 2))
    return exemplars

def handly_select_exemplars_of1_little():
    np_images = get_numbers_of_type(the_number=1)
    indexes = [94,101,100]
    exemplars = list([np_images[ind] for ind in indexes])
    draw_several(exemplars, indexes, rows=1, cols=int(len(indexes) ))
    return exemplars

def handly_select_exemplars_of4():
    np_images = get_numbers_of_type(the_number=4)
    indexes = [94,101,100]
    exemplars = list([np_images[ind] for ind in indexes])
    #draw_several(exemplars, indexes, rows=1, cols=int(len(indexes) ))
    return exemplars

def handly_select_exemplars_of6():
    np_images = get_numbers_of_type(the_number=6)
    indexes = [220,221,222,235,330]
    exemplars = list([np_images[ind] for ind in indexes])
    draw_several(exemplars, indexes, rows=1, cols=int(len(indexes) ))
    return exemplars

def get_diverse_set_of_numbers(n):
    mnist_train = get_train_mnist()
    np_images = mnist_train.train_data.numpy()[0:n]
    #draw_several(np_images[0:35], list(range(0,35)), rows=5, cols=7)
    return np_images


