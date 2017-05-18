import copy
import cv2
import numpy as np
import sys

conv = [[-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0]]

if (len(sys.argv) == 3):
    img = cv2.imread(sys.argv[1], 0)
    rows = img.shape[0]
    cols = img.shape[1]
    # creamos una copia de la imagen original para el volcado de informacion
    img2 = copy.copy(img)
    cv2.imshow('original', img)
    # para cada pixel aplicamos la matriz del filtro
    for rowss in range(0, rows, 1):
        for colss in range(0, cols, 1):
            value = 0
            value += img2[rowss, colss] * conv[1][1]
            if rowss > 0:
                value += (img2[rowss - 1, colss] * conv[0][1])
            if colss > 0:
                value += (img2[rowss, colss - 1] * conv[1][0])
            if rowss < rows - 2:
                value += (img2[rowss + 1, colss] * conv[2][1])
            if colss < cols - 2:
                value += (img2[rowss, colss + 1] * conv[1][2])
            if colss > 0 and rowss > 0:
                value += (img2[rowss - 1, colss - 1] * conv[0][0])
            if rowss > 0 and colss < cols - 2:
                value += (img2[rowss - 1, colss + 1] * conv[0][2])
            if colss > 0 and rowss < rows - 2:
                value += (img2[rowss + 1, colss - 1] * conv[2][0])
            if rowss < rows - 2 and colss < cols - 2:
                value += (img2[rowss + 1, colss + 1] * conv[2][2])
            img[rowss, colss] = int(np.clip(value, 0, 255))
            # para limitar el valor, npclip lo limita a un maximo y un minimo

    r = cv2.imshow('filtrada', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
