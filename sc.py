import matplotlib.pyplot as plt
import numpy as np
import os, sys
from imageio import imread, imwrite


def main():

    #img = imread(sys.argv[1])
    #img = imread('dice.png')
    #print(img)
    def write(file):
        img = imread(file)
        imwrite('dice2.png', img[:len(img)//2])

if __name__ == '__main__':
    main()
