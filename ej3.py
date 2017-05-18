import cv2
import numpy as np
import sys

if (len(sys.argv) == 4):
    img2 = np.zeros((int(sys.argv[1]), int(sys.argv[2]), 3), np.uint8)
    cv2.circle(img2, (int(sys.argv[1]) / 2, int(sys.argv[2]) / 2), 50, (0, 0, 255), 0)
    cv2.circle(img2, (int(sys.argv[1]) / 2, int(sys.argv[2]) / 2), 40, (0, 255, 0), -1)
    cv2.line(img2, (0, 0), (int(sys.argv[1]), int(sys.argv[2])), (255, 0, 0), 3)
    pts = np.array([[100, 50], [200, 300], [70, 200], [50, 100]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img2, [pts], True, (0, 255, 255))
    cv2.imwrite(sys.argv[3], img2)
    r = cv2.imshow('image', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print ("Error en los parametros.")
