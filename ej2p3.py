import cv2
import numpy as np
import sys

if (len(sys.argv) == 3):
    img = cv2.imread(sys.argv[1], 0)
    rows = img.shape[0]
    cols = img.shape[1]
    hist = np.zeros(256, np.uint8)
    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            hist[img[rowss, colss]] += 1
    img2 = np.zeros((500, 500), np.uint8)
    img2[:] = (255)
    min = 0
    max = 0
    for i in range(0, 255, 1):
        for j in range(hist[i]):
            img2[490 - j, 10 + i] = 0
    cv2.imwrite("historiginal.jpg", img2)
    for i in range(0, 255, 1):
        if (hist[i] == 0):
            min = i
        else:
            break

    for i in range(255, 0, -1):
        if (hist[i] == 0):
            max = i
        else:
            break
    a = float(255.0 / (max - min))
    b = float(-(min * a))

    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            img[rowss, colss] = (a * img[rowss, colss]) + b

    hist = np.zeros(256, np.uint8)
    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            hist[img[rowss, colss]] += 1
    img2 = np.zeros((500, 280), np.uint8)
    img2[:] = (255)
    min = 0
    max = 0
    for i in range(0, 255, 1):
        for j in range(hist[i]):
            img2[490 - j, 10 + i] = 0
    cv2.imwrite(sys.argv[2], img2)
    r = cv2.imshow('image', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
