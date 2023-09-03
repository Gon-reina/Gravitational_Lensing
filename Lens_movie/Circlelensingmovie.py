"""
@author: Gonzalo Reina
student id: 14280757
"""
#Import the functions and necessary modules
import numpy as np
import matplotlib.pyplot as plt
from lensingmovie import lensing
import os
import cv2

#Find path to folder to save the frames
framefolder = os.getcwd()
framefolder = framefolder + '\\frames' 

#Define size of the drames
size = 255

#Define the image array
imsize = (size,size)
#Create x and y coordinates
x = np.arange(0,imsize[1])
y = np.arange(0,imsize[0])
X, Y = np.meshgrid(x,y)
#Choose a scale length fo the brightness profile
a = 10
#Choose range of motion
offset = -1*np.linspace(-70, 70, 20)
video = cv2.VideoWriter('lensmovie.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 20, imsize)

for n,yoffset in enumerate(offset):
    #Create array for the frame
    img = np.zeros((imsize))
    #Add the circle to the frame
    img = img + 3*np.exp(-np.sqrt((X-np.ceil(size/2))**2+(Y-np.ceil(size/2)+yoffset)**2)/a)
    #Number the frame
    notlensedtitle = framefolder + '\\notlensed-' + str(n) + '.png' 
    # #Save  the image with an appropiate colormap
    img = plt.imsave(notlensedtitle,img, cmap = 'nipy_spectral')
    img = plt.imread(notlensedtitle)
    #Lens the frame and save it
    k = 0
    lensed_img = lensing(img, k)
    lensedtitle = framefolder + '\\lens-' + str(n) + '.png'
    plt.imsave(lensedtitle,lensed_img, cmap = 'nipy_spectral')
    #Add frame to the video
    frame = cv2.imread(lensedtitle)
    video.write(frame)
#Save video
video.release()
