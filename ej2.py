import cv2
import numpy as np
import sys

if (len(sys.argv) == 3):
    img = cv2.imread(sys.argv[1])
    rows = img.shape[0]
    cols = img.shape[1]
    img2 = np.zeros((rows, cols, 3), np.uint8)
    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            img2[rowss, -colss] = img[rowss, colss]
    cv2.imwrite(sys.argv[2], img2)
    r = cv2.imshow('image', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
