import cv2
import numpy as np 

# 替换像素点
img=cv2.imread('C:/Users/admin/Desktop/cv/HR.jpg',cv2.IMREAD_COLOR)
# px=img[100,100]
# print(px)
# blue=img[100,100,0]
# print(blue)
# img[101,101]=[255,255,255]
# print(img[101,101])
print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))


#图像ROI region of interest
img=cv2.imread('C:/Users/admin/Desktop/cv/flower.jpg',cv2.IMREAD_COLOR)
flower=img[160:180,160:180]
img[10:30,10:30]=flower
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#拆分合并通道
# r,g,b=cv2.split(img)
# img=cv2.merge(r,g,b)

# b=img[:,:,0]
# img[:,:,2]=0


#图像扩边
import matplotlib.pyplot as plt 
img=cv2.imread('C:/Users/admin/Desktop/cv/flower.jpg',cv2.IMREAD_COLOR)
blue = [255,0,0]
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)#复制最后一个元素
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)#边界元素的镜像
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=blue)#带颜色的常数

plt.subplot(231),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')

plt.show()
