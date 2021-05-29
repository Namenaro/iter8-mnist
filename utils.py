import numpy as np
import matplotlib.pyplot as plt
import torchvision.datasets as datasets

def get_train_mnist():
    mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
    return mnist_trainset

def draw_several(np_images, np_labels):
    plt.figure()
    rows = 5
    cols = 7
    num_of_images = rows*cols
    for index in range(1, num_of_images + 1):
        plt.subplot(rows, cols, index)
        plt.axis('off')
        if np_labels is not None:
            plt.title(np_labels[index])
        plt.imshow(np_images[index].squeeze(), cmap='gray_r')
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