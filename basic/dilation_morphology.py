import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('C:/Users/admin/Desktop/cv/rose.jpg')
kernel = np.ones((5,5),np.uint8)

# 腐蚀，去白噪，连接断开的物体
erosion = cv2.erode(img,kernel,iterations=1)
while(1):
    cv2.imshow('image',img)
    cv2.imshow('erosion',erosion)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()


# 膨胀扩张，也可以连接两个分开的物体
# 一般先去噪，再扩张
dilation = cv2.dilate(img,kernel,iterations=1)
while(1):
    cv2.imshow('image',img)
    cv2.imshow('dilation',dilation)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()


# 开运算，先腐蚀后膨胀，用来去噪
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
while(1):
    cv2.imshow('image',img)
    cv2.imshow('opening',opening)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()


# 闭运算，先膨胀后腐蚀，用来填充前景物体的小洞，或者小黑点
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
while(1):
    cv2.imshow('image',img)
    cv2.imshow('closing',closing)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()


# 形态学梯度，膨胀与腐蚀的差别，看起来像前景物体的轮廓
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
while(1):
    cv2.imshow('image',img)
    cv2.imshow('gradient',gradient)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()


# 礼帽，原图像与进行开运算之后的图像的差
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
while(1):
    cv2.imshow('image',img)
    cv2.imshow('tophat',tophat)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()


# 黑帽，原图像与进行闭运算之后的图像的差
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
while(1):
    cv2.imshow('image',img)
    cv2.imshow('blackhat',blackhat)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
cv2.destroyAllWindows()

# 构建不同的核
print(cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))
print(cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))