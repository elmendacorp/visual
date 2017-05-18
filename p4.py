import cv2
import numpy as np
import sys

if (len(sys.argv) == 3):
    img = cv2.imread(sys.argv[1], 0)
    rows = img.shape[0]
    cols = img.shape[1]
    hist = [0] * 256
    cv2.imshow('original', img)
    # Calculo el histograma de la imagen original
    for rowss in range(0, rows, 1):
        for colss in range(0, cols, 1):
            hist[img[rowss, colss]] += 1
    # Calculo la transformacion de forma que a un tono le corresponde una probabilidad de estar en una posicion
    trans = np.zeros(256, np.uint8)
    probabilidades = np.zeros(256)
    for i in range(0, 256, 1):
        probabilidades[i] = np.round(float(hist[i]) / (rows * cols), 5)
    # para cada tono calculamos su nueva posicion basada en su probabilidad
    acumula = 0.0
    for j in range(0, 256, 1):
        acumula += float(probabilidades[j])
        trans[j] = int(acumula * 256)
    # aplicamos la transformacion
    for rowss in range(0, rows, 1):
        for colss in range(0, cols, 1):
            img[rowss, colss] = trans[(img[rowss, colss])]

    r = cv2.imshow('ecualizada', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
