import numpy as np
import cv2
import math
import sys, getopt

def thesquare(x,y,size, img):
    l=size/2
    pts = np.array([[math.floor(x-l),math.floor(y-l)],[math.floor(x+l),math.floor(y-l)],[math.floor(x+l),math.floor(y+l)],[math.floor(x-l),math.floor(y+l)]], np.int32)
    cv2.fillConvexPoly(img,pts,(0,0,255))
   # cv2.polylines(img,[pts],True,(0,0,255))

def squaring(i,j,sz,img):
    if(sz <10):
        return
    s=sz/2
    x1=i-sz/2-s/2
    y1=j
    x2=i
    y2=j-sz/2-s/2
    x3=i
    y3=j+sz/2+s/2
    x4=i+sz/2+s/2
    y4=j
    thesquare(x1,y1,s,img)
    squaring(x1,y1,s,img)
    thesquare(x2,y2,s,img)
    squaring(x2,y2,s,img)
    thesquare(x3,y3,s,img)
    squaring(x3,y3,s,img)
    thesquare(x4,y4,s,img)
    squaring(x4,y4,s,img)


def main():
    if(len(sys.argv) < 2):
        print("enter desired size")
        sys.exit(2)
    size = int(sys.argv[1])
    img = np.zeros([size,size,3])
    ss=size/5
    thesquare(size/2,size/2,ss,img)
    squaring(size/2,size/2,ss,img)
    cv2.imshow("image",img)
    cv2.waitKey()
if __name__ == "__main__":
    main()
