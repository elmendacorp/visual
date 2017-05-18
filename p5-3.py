import cv2
import numpy as np
import sys
#funcion que calcula el histograma de una zona
def histograma(imagen,m,n, m_inicio,n_inicio):
    histo = np.zeros(256, np.uint8)
    for colss in range(m_inicio, m_inicio+m-1, 1):
        for rowss in range(n_inicio, n_inicio+n-1, 1):
            histo[imagen[rowss, colss]] += 1
    return histo
#funcion que umbraliza una zona
def umbraliza(imagen,umbral,x,y,x_inicio,y_inicio):
    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            if imagen[rowss, colss] < umbral:
                imagen[rowss, colss] = 0
            else:
                imagen[rowss, colss] = 255

if (len(sys.argv) == 5):
    img = cv2.imread(sys.argv[1], 0)
    rows = img.shape[0]
    cols = img.shape[1]
#seleccion metodo general
    if(sys.argv[4]=="general"):
        m=int(sys.argv[2])
        n=int(sys.argv[3])
        for i in range(0,rows,np.round(rows/m,0)):
            for j in range(0,cols,np.round(cols/n,0)):
                hist=histograma(img,m,n,np.clip(i,0,rows-1),np.clip(j,0,cols-1))

        umbral = 256 / 2
        for pasadas in range(0, int(sys.argv[2]), 1):
            g1 = 0
            g2 = 0
            for sub1 in range(0, umbral, 1):
                g1 += hist[sub1]
            m1 = g1 / umbral
            for sub2 in range(umbral, 255, 1):
                g2 += hist[sub2]
            m2 = g2 / (256 - umbral)
            umbral = np.round(((m1 + m2) / 2), 0)
        print("el umbral es:", umbral)
#seleccion metodo otsu
    if (sys.argv[4] == "otsu"):
        umbral = 256 / 2
        for pasadas in range(0, int(sys.argv[2]), 1):
            g1 = 0
            g2 = 0
            for sub1 in range(0, umbral, 1):
                g1 += hist[sub1]
            m1 = g1 / umbral
            for sub2 in range(umbral, 255, 1):
                g2 += hist[sub2]
            m2 = g2 / (256 - umbral)
            umbral = np.round(((m1 + m2) / 2), 0)
        print("el umbral es:", umbral)


    else:
        print("Error en el metodo")
        exit(0)
    r = cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
