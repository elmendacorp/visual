import cv2
from numpy import *
#funcion para pintar las lineas de flujo
def draw_flow(im,flow,step=16):
    h,w = im.shape[:2]
    y,x = mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
    fx,fy = flow[y,x].T

    #Calculamos el final de las lineas
    lines = vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines = int32(lines)

    # Creamos la imagen y pintamos las lineas y las agujas
    vis = cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
    for (x1,y1),(x2,y2) in lines:
        cv2.line(vis,(x1,y1),(x2,y2),(0,255,0),1)
        cv2.circle(vis,(x1,y1),1,(0,255,0), -1)
    return vis

#iniciamos la captura de video
cap = cv2.VideoCapture(0)

ret,im = cap.read()
prev_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

while True:
    # Convertimos a escala de grises
    ret,im = cap.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    #calculamos el flujo
    flow = cv2.calcOpticalFlowFarneback(prev_gray,gray,float(0),float(0),3,15,3,5,float(1),0)
    prev_gray = gray

    # Pintamos el resultado por pantalla
    cv2.imshow('Optical flow',draw_flow(gray,flow))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break