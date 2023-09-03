def lensing(img, k): 
   
    import matplotlib.pyplot as plt
    import numpy as np
    
    

    lensed_img = img*0

    
    X = np.linspace(-5, 5, img.shape[1])
    Y = np.linspace(-5, 5, img.shape[0])
    
    #Define physical constants and set them to SI units
    h = 6.626e-34
    pc = 3.086e16
    c = 3e8
    sigma = 1500e3
    Dls = (441e6)*(pc/h)
    Ds = (878e6)*(pc/h)
    Rc = (70e3)*(pc/h)
    Dl = (637e6)*(pc/h)
    Te = 4*np.pi*(sigma**2)*Dls/(Ds*c**2)
    
    #Define Einstein radius
    rc = Rc/(Dl*Te)

    
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
    lensed_img = plt.imread('lensedoutput.png')
    return lensed_img
