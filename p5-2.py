import cv2
import numpy as np
import sys

if (len(sys.argv) == 2):
    img = cv2.imread(sys.argv[1], 0)
    rows = img.shape[0]
    cols = img.shape[1]
    hist = [0] *256
    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            hist[img[rowss, colss]] +=1
    #calculo de las probabilidades
    prob =[0] *256
    var= rows*cols
    for i in range(0,255,1):
        prob[i]=float(hist[i])/var

    #calculo de los momentos
    omega =[0] *256
    mul =[0] *256
    omega[0]=prob[0]
    for i in range(1,256,1):
        omega[i]= omega[i-1]+prob[i]
        mul[i]=mul[i-1]+(i-1)*prob[i]

    sigmaB2max = 0
    sigmaB2 = 0
    mut = mul[255]
    umbralOptimo = 0
    for t in range(0,256,1):
        omega1 = omega[t]
        omega2 = 1 - omega1
        if omega1!=0 and omega2!=0:
            mu1 = mul[t] / omega1
            mu2 = (mut - mul[t]) / omega2
            sigmaB2 = omega1 * (mu1 - mut)*(mu1 - mut) + omega2*(mu2 - mut)*(mu2 - mut)
            if sigmaB2 > sigmaB2max:
                sigmaB2max = sigmaB2
                umbralOptimo = t - 1

    print("el umbral es:",umbralOptimo)
    for colss in range(0, cols, 1):
        for rowss in range(0, rows, 1):
            if img[rowss, colss] < umbralOptimo:
                img[rowss, colss]=0
            else:
                img[rowss, colss]=255
    r = cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
