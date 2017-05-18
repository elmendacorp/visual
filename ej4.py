import cv2
import sys

if (len(sys.argv) == 2):
    cap = cv2.VideoCapture(sys.argv[1])
    while (cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow(sys.argv[1], frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

else:
    print ("Error en los parametros.")
