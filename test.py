import cv2
import sys

if (len(sys.argv) == 3):
    img = cv2.imread(sys.argv[1])
    rows = img.shape[0]
    cols = img.shape[1]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))

    r = cv2.imshow('image', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
