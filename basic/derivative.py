import cv2
import numpy as np 
import matplotlib.pyplot as plt 


# Sobel算子是高斯平滑与微分操作的结合体
# Scharr只作用于size=3的内核，一样快，而且更加精确
# Laplacians，二阶
img = cv2.imread('C:/Users/admin/Desktop/cv/rose.jpg',0)
# output size=-1，the same depth as the source, it will result in truncated derivatives
laplacian=cv2.Laplacian(img,cv2.CV_64F)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
scharr=cv2.Scharr(img,cv2.CV_64F,1,0)

# plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
# plt.title('original'),plt.xticks([]),plt.yticks([])

plt.subplot(2,2,1),plt.imshow(scharr,cmap='gray')
plt.title('scharr'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
plt.title('Sobel X'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])

plt.show()