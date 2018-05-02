import cv2 
import numpy as np 
import matplotlib.pyplot as plt 


img = cv2.imread('C:/Users/admin/Desktop/cv/rose.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image ,contours,hierarchy = cv2.findContours(thresh,2,1)
cnt=contours[0]

hull=cv2.convexHull(cnt,returnPoints=False)
defects=cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0]
    start=tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    far=tuple(cnt[f][0])
    cv2.line(img,start,end,[155,255,155],2)
    cv2.circle(img,far,5,[255,0,255],-1)
while(1):
    cv2.imshow('img',img)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()

print(cv2.pointPolygonTest(cnt,(50,50),True))
# Flase 只返回+1，-1，0


# 形状匹配
# img1 = cv2.imread('C:/Users/admin/Desktop/cv/rose.jpg')
# img2 = cv2.imread('C:/Users/admin/Desktop/cv/flower.jpg')

# ret,thresh=cv2.threshold(img1,127,255,0)
# ret,thresh2=cv2.threshold(img2,127,255,0)
# contours,hierarchy =cv2.findContours(thresh,2,1)
# cnt1=contours[0]
# contours,hierarchy =cv2.findContours(thresh2,2,1)
# cnt2=contours[0]
# ret=cv2.matchShapes(cnt1,cnt2,1,0,0)
# print(ret)