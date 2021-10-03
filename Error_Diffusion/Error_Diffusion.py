import numpy as np
import cv2

def floyd_steinberg_kernel(arr):
    floyd_steinberg = np.array([
        [0, 0, 7],
        [3, 5, 1]
    ])

    y_dim = int(arr.shape[0])
    x_dim = int(arr.shape[1])
    diffused_fs_img = np.array(np.double(arr))

    for y in range(y_dim):
        for x in range(x_dim):
            original = diffused_fs_img[y, x]
            error = 0
            if original < 128:
                diffused_fs_img[y, x] = 0
                error = original-0
            else:
                diffused_fs_img[y, x] = 255
                error = original-255
            element_sum = 0
            for i in range(2, 6):
                if y + (i // 3) < 512 and x + ((i % 3)-1) >= 0 and x + ((i % 3)-1) < 512:
                    element_sum += floyd_steinberg[(i // 3), (i % 3)]
            # print(element_sum)
                
            for i in range(2, 6):
                if y + (i // 3) < 512 and x + ((i % 3)-1) >= 0 and x + ((i % 3)-1) < 512:
                    error_diffus = error * floyd_steinberg[(i // 3), (i % 3)] / element_sum
                    diffused_fs_img[(y + (i // 3)), (x + ((i % 3)-1))] += error_diffus 
    cv2.imwrite('Error_Diffusion_Floyd_Steinberg.bmp', diffused_fs_img)
                
def jarvis_kernel(arr):
    jarvis = np.array([
        [0, 0, 0, 7, 5],
        [3, 5, 7, 5, 3],
        [1, 3, 5, 3, 1]
    ])

    y_dim = int(arr.shape[0])
    x_dim = int(arr.shape[1])
    diffused_j_img = np.array(np.double(arr))

    for y in range(y_dim):
        for x in range(x_dim):
            original = diffused_j_img[y, x]
            error = 0
            if original < 128:
                diffused_j_img[y, x] = 0
                error = original-0
            else:
                diffused_j_img[y, x] = 255
                error = original-255
            element_sum = 0
            for i in range(3, 15):
                if y + (i // 5) < 512 and x + ((i % 5)-2) >= 0 and x + ((i % 5)-2) < 512:
                    element_sum += jarvis[(i // 5), (i % 5)]
                
            for i in range(3, 15):
                if y + (i // 5) < 512 and x + ((i % 5)-2) >= 0 and x + ((i % 5)-2) < 512:
                    error_diffus = error * jarvis[(i // 5), (i % 5)]/element_sum
                    diffused_j_img[(y + (i // 5)), (x + ((i % 5)-2))] += error_diffus 
    cv2.imwrite('Error_Diffusion_Jarvis.bmp', diffused_j_img)

def stucki_kernal(arr):
    stucki = np.array([
        [0, 0, 0, 8, 4],
        [2, 4, 8, 4, 2],
        [1, 2, 4, 2, 1]
    ])

    y_dim = int(arr.shape[0])
    x_dim = int(arr.shape[1])
    diffused_s_img = np.array(np.double(arr))

    for y in range(y_dim):
        for x in range(x_dim):
            original = diffused_s_img[y, x]
            error = 0
            if original < 128:
                diffused_s_img[y, x] = 0
                error = original-0
            else:
                diffused_s_img[y, x] = 255
                error = original-255
            element_sum = 0
            for i in range(3, 15):
                if y + (i // 5) < 512 and x + ((i % 5)-2) >= 0 and x + ((i % 5)-2) < 512:
                    element_sum += stucki[(i // 5), (i % 5)]
                
            for i in range(3, 15):
                if y + (i // 5) < 512 and x + ((i % 5)-2) >= 0 and x + ((i % 5)-2) < 512:
                    error_diffus = error * stucki[(i // 5), (i % 5)]/element_sum
                    diffused_s_img[(y + (i // 5)), (x + ((i % 5)-2))] += error_diffus 
    cv2.imwrite('Error_Diffusion_Stucki.bmp', diffused_s_img)

if __name__ == "__main__":
    img = cv2.imread("lena.bmp")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    floyd_steinberg_kernel(img)
    jarvis_kernel(img)
    stucki_kernal(img)
    