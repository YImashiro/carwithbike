import cv2
import numpy as np
import copy

grav = (0,0)
left_coord,center_coord,right_coord = (0,0),(0,0),(0,0)
angle = 0

def pink_detect(img):
    '''RGBtoHSV
    threshold for pink_ball
    [HUE(0to179) threshold should be 0to15,
    Saturation [0,255],Lightness[0,255]
    target may be [327/2,255*0.92,255]'''
    
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    pink_min = np.array([170,130,130])
    pink_max = np.array([179,255,255])
    
    mask1 = cv2.inRange(hsv, pink_min,pink_max)

    pink_min2 = np.array([0,130,130])
    pink_max2 = np.array([9,255,255])

    mask2 = cv2.inRange(hsv,pink_min2,pink_max2)
    return mask1 + mask2

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
    global grav
    cap = cv2.VideoCapture(0)
    try:
        while(cap.isOpened()):
            #_:T or F, frame:frame
            print(grav)
            _, frame = cap.read()
            height = frame.shape[0]
            width = frame.shape[1]
            #cv2.GaussianBlur(img,filter_range,variance)
            mask = pink_detect(cv2.GaussianBlur(frame,(25,25),3))
            rect = find_target(mask)
            drawrect = cv2.rectangle(frame,tuple(rect[0:2]),(rect[0]+rect[2],rect[1]+rect[3]), (0,0,255), thickness=2)
            grav = (int(rect[0]+rect[2]/2),int(rect[1]+rect[3]/2))

            cv2.line(drawrect,(int(width/2),0),(int(width/2),int(height)),(255,0,0),5)
            cv2.circle(drawrect,grav, 3, (255, 255, 0), 5) 
            cv2.imshow("rect",drawrect)
            cv2.moveWindow('rect', 1000, 0)
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except:
        print("exception")
    finally:
        cap.release()
        cv2.destroyAllWindows()
    return grav

def coordtoangle(left_coordx,center_coordx,right_coordx,gravx):
    if gravx < center_coordx + 10 and gravx > center_coordx - 10:
        angle = 0
    elif gravx > center_coordx:
        if (gravx > left_coordx):
            gravx = left_coordx
        angle =  (center_coordx - gravx)/(left_coordx - center_coordx) * 50
    else:
        if (gravx < right_coordx):   
            gravx = right_coordx
        angle = (gravx - center_coordx) / (right_coordx - center_coordx) * 50
    return int(angle)

        
def setting():
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
    print(left_coord,center_coord,right_coord)
    return left_coord,center_coord,right_coord

if __name__ == "__main__":
    left_coord,center_coord,right_coord = setting()
    anlge = coordtoangle(left_coord[0],center_coord[0],right_coord[0],grav[0])
