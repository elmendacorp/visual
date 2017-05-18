import cv2
import numpy as np
import sys

if (len(sys.argv) == 2):
    img = cv2.imread(sys.argv[1], 0)
    rows = img.shape[0]
    cols = img.shape[1]
    hist = np.zeros(256, np.uint8)
    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            hist[img[rowss, colss]] += 1
    print hist
else:
    print ("Error en los parametros.")
