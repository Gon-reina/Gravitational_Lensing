from lensingprogramme import lensing
import matplotlib.pyplot as plt
import numpy as np

#Create single pixel image
imsize = (254,254)
whitepix = np.zeros((imsize))
whitepix[127,127] = 255
whitepix[126,126] = 255
whitepix[126,127] = 255
whitepix[127,126] = 255
plt.imsave('whitepixel.png',whitepix, cmap = 'gray')
whitepix = plt.imread('whitepixel.png')

k = 0
lensed_img = lensing(whitepix, k)

fig = plt.figure()
ax1 = plt.subplot(121)
ax1.title.set_text('Source image')
ax2 = plt.subplot(122)
ax2.title.set_text('Lensed image')
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
ax1.imshow(whitepix, extent = (-1,1,-1,1))
ax2.imshow(lensed_img, extent = (-1,1,-1,1))
plt.show()

numWhitePixel = np.sum(lensed_img[:,:,2]==1)
