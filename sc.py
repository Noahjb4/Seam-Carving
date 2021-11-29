import matplotlib.pyplot as plt
import numpy as np
import os, sys
from imageio import imread, imwrite

class Image():
    def __init__(self, file):
        self.file = file
        self.img = imread(self.file)

    def write(self):
            imwrite('test.png', self.img[:len(self.img)//2])

# def main():

#     #img = imread(sys.argv[1])
#     #img = imread('dice.png')
#     #print(img)
    

# if __name__ == '__main__':
#     main()
