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
    umbral= 256/2
    for pasadas in range(0,int(sys.argv[2]),1):
        g1=0
        g2=0
        for sub1 in range(0,umbral,1):
            g1+=hist[sub1]
        m1=g1/umbral
        for sub2 in range(umbral,255,1):
            g2+=hist[sub2]
        m2 = g2 / (256-umbral)
        umbral=np.round(((m1+m2)/2),0)
    print("el umbral es:",umbral)
    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            if img[rowss, colss] < umbral:
                img[rowss, colss]=0
            else:
                img[rowss, colss]=255
    r = cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
