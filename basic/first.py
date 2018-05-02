import cv2
import numpy as np 

#read
img=cv2.imread('C:/Users/admin/Desktop/cv/HR.jpg',cv2.IMREAD_COLOR)#color
img2=cv2.imread('C:/Users/admin/Desktop/cv/HR.jpg',cv2.IMREAD_GRAYSCALE)#gray
cv2.namedWindow('image',cv2.WINDOW_NORMAL)#the window for the picture, fit the size

#show
cv2.imshow('image',img2)
cv2.waitKey(0)#wait the keyboard 
cv2.destroyAllWindows()#delete the windows
#write
cv2.imwrite('C:/Users/admin/Desktop/cv/HR.png',img2)


cv2.imshow('image',img)
k=cv2.waitKey(0)&0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('C:/Users/admin/Desktop/cv/HR1.png',img)
    cv2.destroyAllWindows()


import matplotlib.pyplot as plt 
img =cv2.imread('C:/Users/admin/Desktop/cv/HR.jpg',0)
plt.imshow(img,cmap='gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])  #to hide tick values on X and Y axis
plt.show()


print(img.shape,img.size,img.dtype)

