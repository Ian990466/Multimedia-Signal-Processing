import cv2
import random
import math
import numpy as np

def distortion():
    
    return

def cluster():
    return

def decoder():
    return

if __name__ == "__main__":
    load_img = cv2.imread("lena.bmp")
    load_img = cv2.cvtColor(load_img, cv2.COLOR_BGR2GRAY)

    img = np.array(load_img)
    y_dim = img.shape[0]
    x_dim = img.shape[1]

    print(img[511,0])
    # Codebook initial Size (Number of codevectors) = Nc
    Nc = 128
    block_x = 512/Nc
    block_y = 512/Nc
    codebook = []

    for block_ix in range(Nc):
        buffer = []
        for block_i in range(block_x * block_y):
            buffer
            

    pass

