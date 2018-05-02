import numpy as np 
import cv2

# #line
# img=np.zeros((512,512,3),np.uint8)

# cv2.line(img,(0,0),(250,250),(255,0,0),5)#coordinate，color，px=5

# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image',1000,1000)#frame
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#rectangle
img=np.zeros((512,512,3),np.uint8)
cv2.rectangle(img,(350,0),(500,128),(10,255,100),3)#左上角和右下角的顶点

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)#frame
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#circle
img=np.zeros((512,512,3),np.uint8)
cv2.circle(img,(300,60),100,(100,100,100),1)#圆心坐标，r

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)#frame
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#ellipse
img=np.zeros((512,512,3),np.uint8)
cv2.ellipse(img,(256,256),(100,50),60,60,360,255,-1)#center,axes,angle,startAngle,endAngle,color

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)#frame
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# polylines
img=np.zeros((512,512,3),np.uint8)
pts=np.array([[10,5],[20,30],[70,20],[50,10],[60,5]],np.int32)
pts=pts.reshape((-1,1,2))#-1表示这一维度的长度是根据后面的维度计算的
cv2.polylines(img,[pts],True,(100,255,255))#False,不闭合的Line

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)#frame
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# font
img=np.zeros((512,512,3),np.uint8)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpneCV',(10,80),font,4,(255,100,200),4,cv2.LINE_AA)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)#frame
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()