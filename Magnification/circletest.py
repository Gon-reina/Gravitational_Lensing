"""
@author: Gonzalo Reina
student id: 14280757
"""
#Import the functions and necessary modules
import matplotlib.pyplot as plt
import numpy as np
from lensingprogramme import lensing


datapoints = 100
offset = -1*np.linspace(-1, 1, datapoints)
numwhite = np.zeros((datapoints, 1))
time = np.zeros((datapoints, 1))

for n,yoffset in enumerate(offset):
    #Creat black image
    imsize = 255
    #Add a white circle to it
    x = np.linspace(-0.8,0.8,imsize)
    y = np.linspace(-0.8,0.8,imsize)
    X, Y = np.meshgrid(x,y)
    arr = np.zeros((y.size, x.size))
    mask = ((X)**2 + (Y+yoffset)**2)**0.5 < 0.2
    arr[mask] = 255
    #Generate image file and lens it
    plt.imsave('circle.png',arr, cmap = 'gray')
    circle = plt.imread('circle.png')
    counto = np.sum(circle[:,:,2])
    k = 0
    lensedcircle = lensing(circle, k)
    #Count the white pixels
    count = np.sum(lensedcircle[:,:,2])
    numwhite[n] = count/counto
    time[n] = n
    
#Show results
plt.figure()
plt.plot(time, numwhite)
plt.xlabel('step')
plt.ylabel('Ratio of white pixels')
plt.show()