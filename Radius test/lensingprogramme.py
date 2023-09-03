def lensing(img, k): 
   
    import matplotlib.pyplot as plt
    import numpy as np
    
    

    lensed_img = img*0

    
    X = np.linspace(-1, 1, img.shape[1])
    Y = np.linspace(-1, 1, img.shape[0])
    
    rc = 0.0001

    
    for n,y in enumerate(Y):
        for p,x in enumerate(X):
            s1 = x - ((1-k)*x)/np.sqrt(rc**2 +(1-k)*x**2 +(1+k)*y**2)
            s2 = y - ((1+k)*y)/np.sqrt(rc**2 +(1-k)*x**2 +(1+k)*y**2)
            diffX = np.abs(X-s1)
            diffY = np.abs(Y-s2)
            ox = np.where(diffX==np.amin(diffX))
            oy = np.where(diffY==np.amin(diffY))
            RGB = img[oy,ox,:]
            lensed_img[n,p,:] = RGB
            
    plt.imsave('lensedoutput.png',lensed_img)
    return lensed_img
