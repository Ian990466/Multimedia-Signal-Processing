import numpy as np
import cv2

def classical_four(arr):
    
    class_arr = np.double([
    0.567, 0.635, 0.608, 0.514, 0.424, 0.365, 0.392, 0.486,
    0.847, 0.878, 0.910, 0.698, 0.153, 0.122, 0.090, 0.302,
    0.820, 0.969, 0.941, 0.667, 0.180, 0.031, 0.059, 0.333,
    0.725, 0.788, 0.757, 0.545, 0.275, 0.212, 0.243, 0.455,
    0.424, 0.365, 0.392, 0.486, 0.567, 0.635, 0.608, 0.514,
    0.153, 0.122, 0.090, 0.302, 0.847, 0.878, 0.910, 0.698,
    0.180, 0.031, 0.059, 0.333, 0.820, 0.969, 0.941, 0.667,
    0.275, 0.212, 0.243, 0.455, 0.725, 0.788, 0.757, 0.545
    ])
    
    y_dim = int(arr.shape[0])
    x_dim = int(arr.shape[1])
    transformed_img_class = np.empty((y_dim, x_dim))

    for y in range(y_dim):
        for x in range(x_dim):
            if arr[y, x] >= class_arr[(x % 8) + (y % 8) * 8] * 255:
                transformed_img_class[y, x] = 255
            elif arr[y, x] < class_arr[(x % 8) + (y % 8) * 8] * 255:
                transformed_img_class[y, x] = 0

    cv2.imwrite('transformed_by_classical_four.bmp', transformed_img_class)

    

def bayer_five(arr):
    bayer = np.double([
    0.513, 0.272, 0.724, 0.483, 0.543, 0.302, 0.694, 0.453,
    0.151, 0.755, 0.091, 0.966, 0.181, 0.758, 0.121, 0.936,
    0.634, 0.392, 0.574, 0.332, 0.664, 0.423, 0.604, 0.362,
    0.060, 0.875, 0.211, 0.815, 0.030, 0.906, 0.241, 0.845,
    0.543, 0.302, 0.694, 0.453, 0.513, 0.272, 0.724, 0.483,
    0.181, 0.758, 0.121, 0.936, 0.151, 0.755, 0.091, 0.966,
    0.664, 0.423, 0.604, 0.362, 0.634, 0.392, 0.574, 0.332,
    0.030, 0.906, 0.241, 0.845, 0.060, 0.875, 0.211, 0.815
    ])
    
    y_dim = int(arr.shape[0])
    x_dim = int(arr.shape[1])
    transformed_img_class = np.empty((y_dim, x_dim))

    for y in range(y_dim):
        for x in range(x_dim):
            if arr[y, x] >= bayer[(x % 8) + (y % 8) * 8] * 255:
                transformed_img_class[y, x] = 255
            elif arr[y, x] < bayer[(x % 8) + (y % 8) * 8] * 255:
                transformed_img_class[y, x] = 0

    cv2.imwrite('transformed_by_bayer_five.bmp', transformed_img_class)

if __name__ == "__main__":
    img = cv2.imread("lena.bmp")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    classical_four(img)
    bayer_five(img)
    # cv2.imwrite('test.bmp', img_arr)
    # print(img_arr)