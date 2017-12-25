import cv2
import numpy as np
import copy

def pink_detect(img):
    '''RGBtoHSV
    threshold for pink_ball
    [HUE(0to179) threshold should be 0to15,
    Saturation [0,255],Lightness[0,255]
    target may be [327/2,255*0.92,255]'''
    
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    pink_min = np.array([155,50,50])
    pink_max = np.array([165,255,255])
    return cv2.inRange(hsv, pink_min,pink_max)

def find_target(mask):
    img,contours,hierarchy  = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rects = []
    maxrect=[0,0,0,0]
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        if rect[2]*rect[3] > maxrect[2]*maxrect[3]:
            maxrect = copy.deepcopy(rect)
    return maxrect

def capturevideo():
    # try:
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        #_:T or F, frame:frame
        _, frame = cap.read()
        height = frame.shape[0]
        width = frame.shape[1]
        #cv2.GaussianBlur(img,filter_range,variance)
        mask = pink_detect(cv2.GaussianBlur(frame,(25,25),3))
        rect = find_target(mask)
        drawrect = cv2.rectangle(frame,tuple(rect[0:2]),(rect[0]+rect[2],rect[1]+rect[3]), (0,0,255), thickness=2)
        grav = (int(rect[0]+rect[2]/2),int(rect[1]+rect[3]/2))
        #print("gravity point: {} , {} ".format(grav[0],grav[1]))
        cv2.line(drawrect,(int(width/2),0),(int(width/2),int(height)),(255,0,0),5)
        cv2.circle(drawrect,grav, 3, (255, 255, 0), 5) 
        cv2.imshow("rect",drawrect)
        cv2.moveWindow('rect', 1000, 0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # except:
        #    pass
        # finally:
    cap.release()
    cv2.destroyAllWindows()
    return grav

def returngrav():
    capturevideo()
    return grav

def setting():
    left_coord,center_coord,right_coord = [],[],[]
    print("First setup. place your handle straight and place light blue point on the center line ")
    center_coord = capturevideo()
    print("place your handle at 45 degrees to the left")
    print("if you have placed,push q")
    left_coord = capturevideo()
    print(left_coord)
    print("Last step. next place your handle at 45 degrees to the right")
    print("if you have placed,push q")
    right_coord = capturevideo()
    print("well done")
    print("your handle sycronizes with car!!")
    
    return left_coord,center_coord,right_coord

setting()
