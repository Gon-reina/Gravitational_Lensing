def galgen(size,NumGal):
    """
@author: Gonzalo Reina
student id: 14280757
"""
#Import the functions and necessary modules
    import numpy as np
    import matplotlib.pyplot as plt
    
    #Define the number of galaxies and the image
    Gal = np.arange(1,NumGal)
    #Choose  which galaxies will be elliptical 
    ell = np.random.uniform(0.6, 0.75)
    e = np.random.choice(Gal, np.int(NumGal*ell))
    #Define the image array
    imsize = (size,size)
    img = np.zeros((imsize))
    #Create x and y coordinates array for the galaxy positions
    x = np.arange(0,img.shape[1])
    y = np.arange(0,img.shape[0])
    X, Y = np.meshgrid(x,y)
    
    # Add the brightness profile of each galaxy
    for p in Gal:
        #Choose a random position (n,m)
        m= np.random.randint(0,img.shape[0]) 
        n= np.random.randint(0,img.shape[1])
        #Choose a random brightness and scale-length 
        fo = np.random.uniform(0, 1)
        a = np.random.uniform(0, 3)
        if np.any(p == e):
            b = np.random.uniform(0, 3)
            theta = np.random.uniform(0, np.pi)
            Xprime = (X-n)*np.cos(theta) - (Y-m)*np.sin(theta)
            Yprime = (Y-m)*np.cos(theta) + (X-n)*np.sin(theta)
            #Add elliptical galaxies
            img = img + fo*np.exp(-np.sqrt(((Xprime)**2/a**2)+((Yprime)**2/b**2))/a)
        else:
            #Add  circular galaxies
            img = img + fo*np.exp(-np.sqrt((X-n)**2+(Y-m)**2)/a)
    
    #Save  the image with an appropiate colormap
    plt.imsave('output.png',img, cmap='hot')
    img = plt.imread('output.png')
    return img
