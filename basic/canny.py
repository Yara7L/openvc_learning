import cv2
import numpy as no 
import matplotlib.pyplot as plt 


# 去噪，高斯滤波器，计算图像梯度（垂直，水平，两条对角线），非极大值抑制，阈值（minVal,maxVal）
img = cv2.imread('C:/Users/admin/Desktop/cv/rose.jpg')
edges=cv2.Canny(img,100,200)
l2=cv2.Canny(img,100,200,L2gradient=True)

# plt.subplot(121),plt.imshow(img,cmap='gray')
# plt.title('original'),plt.xticks([]),plt.yticks([])

plt.subplot(121),plt.imshow(l2,cmap='gray')
plt.title('L2griandent'),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('edge'),plt.xticks([]),plt.yticks([])

plt.show()