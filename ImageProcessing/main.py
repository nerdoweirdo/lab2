import numpy as np
import matplotlib.pyplot as plt
import os.path
import re

from PIL import Image

def grayscale(Path):
    img_arr = np.asarray(Image.open(Path))
    r = img_arr[:, :, 0]
    print("R:\nmax = " + str(r.max()) + "; min = " + str(r.min()) + "; average = " + str(r.mean()))
    g = img_arr[:, :, 1]
    print("G:\nmax = " + str(g.max()) + "; min = " + str(g.min()) + "; average = " + str(g.mean()))
    b = img_arr[:, :, 2]
    print("B:\nmax = " + str(b.max()) + "; min = " + str(b.min()) + "; average = " + str(b.mean()))
    arr = (img_arr * np.array([0.299, 0.587, 0.114])).astype('uint8')
    arr = np.uint8(np.apply_along_axis(sum, 2, arr))
    new_img = Image.fromarray(arr)
    Path = Path.replace("Lena.png", 'Lena_grayscaled.png')
    new_img.save(Path)
    return arr

def thresholded(Path, arr):
    arr[arr < 100] = 0
    new_img_th = Image.fromarray(arr)
    Path = Path.replace("Lena.png", 'Lena_thresholded.png')
    new_img_th.save(Path)
    return arr

def histogram(arr):
    ax = plt.subplot()
    ax.set_xlabel("Brightness")
    ax.set_ylabel("Amount of pixels")
    ax.hist(arr)
    plt.title("Brightness distribution histogram")
    plt.show()

if __name__ == '__main__':
    Path = input("Input path to the file: ")
    flag = True
    if re.search(r'\.png$', Path):
        flag = True
    else:
        flag = False
        while (flag == False):
            print("Incorrect extension.\n")
            Path = ''
            Path = input("Try again: ")
            if re.search(r'\.png$', Path):
                flag = True
            else:
                flag = False
    arr = grayscale(Path)
    arr = thresholded(Path, arr)
    histogram(arr)
