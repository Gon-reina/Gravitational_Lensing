"""
@author: Gonzalo Reina
student id: 14280757
"""
#Import the functions and necessary modules
from galaxygenerator import galgen
from lensingprogramme import lensing
import matplotlib.pyplot as plt

#Choose an image size and the number of galaxies
size = 254
NumGal = 200
#Generate the image and lens it with ellipticity k
img = galgen(size,NumGal)
k = 0.6
lensed_img = lensing(img, k)

#Show results
fig = plt.figure()
ax1 = plt.subplot(121)
ax1.title.set_text('Source image')
ax2 = plt.subplot(122)
ax2.title.set_text('Lensed image')
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
ax1.imshow(img, extent = (-1,1,-1,1))
ax2.imshow(lensed_img, extent = (-5,5,-5,5))
plt.show()

