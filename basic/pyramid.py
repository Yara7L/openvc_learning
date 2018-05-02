import cv2 
import numpy as np 
import matplotlib.pyplot as plt 


# pyrDown,丢失，分辨率降低,信息会丢失
img = cv2.imread('C:/Users/admin/Desktop/cv/rose.jpg')
lower_reso=cv2.pyrDown(img)
higher_reso2=cv2.pyrUp(img)

while(1):
    cv2.imshow('img',img)
    cv2.imshow('lower_reso',lower_reso)
    cv2.imshow('higher_reso2',higher_reso2)
    if cv2.waitKey()==ord('q'):
        break   
cv2.destroyAllWindows()


# 水果融合