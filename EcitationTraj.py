#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math

def Excitation_Trajectory (t):
    
    nH = 6 #the number of harmonics

    wf = 2*math.pi*0.08
    
    a = np.array([[0.53, -0.01, 0.17, 0.08, 0.60, 0.20],
        [0.43, -0.19, 0.34, 0.24, 0.11, 0.05],
        [0.00,0.55, -0.12, 0.39, -0.13, -0.07],
        [0.32, -0.20, -0.50, 0.17, 0.06, -0.15],
        [0.06, -0.03, -0.41, -0.02, 0.65, 0.68],
        [0.48, 0.03, 0.32, 0.13, 0.04, 0.20],
        [0.79, 0.70, 0.08, 0.02, 1.22, -0.28]]) #aik and bik are the Fourier coefficients

    b = np.array([[-0.38, -0.17, 0.21, 0.11, -0.35, 0.15],
        [-0.04, 0.19, -0.43, -0.19, -0.45, 0.36],
        [0.38, 1.21, 0.27, 0.55, 0.06, -0.32],
        [-0.44, -0.00, 0.58, -0.10, 0.46, 0.01],
        [-0.36, 0.66, 0.43, -0.18, -0.14, -0.14],
        [-0.07, 0.55, 0.38, 0.19, 0.45, 0.15],
        [0.40, -0.13, 0.31, 0.79, -0.09, 0.49]]);
 
    q0 = np.array([0.5,-0.11,0.54,1.76,-1.28,-0.11,0.42])
    #print(a[:,1]@np.cos(wf*1j*t).T)
    for i in range (nH):
        q  += (a[:,i]*(1/wf*1j)).reshape(7,1)@np.sin(wf*1j*t).reshape(1,4000) - (b[:,i]/wf*1j).reshape(7,1)@np.cos(wf*1j*t).reshape(1,4000) + q0.reshape(7,1)
        qd +=  a[:,i].reshape(7,1)@np.cos(wf*1j*t).reshape(1,4000) - b[:,i].reshape(7,1)@np.sin(wf*1j*t).reshape(1,4000)
        qdd += -(a[:,i]*wf*1j).reshape(7,1)@np.sin(wf*1j*t).reshape(1,4000) + (b[:,i]*wf*1j).reshape(7,1)@np.cos(wf*1j*t).reshape(1,4000)
    
    return q, qd, qdd


td = 20 #time duration in second
Fr = 200 #Sample frequency
N = td*Fr #N sample

t = np.linspace(0,td,N)
        
q, qd, qdd = Excitation_Trajectory (t) 


# In[2]:


import numpy as np
import math

a = np.array([[1,2],[1,2]])
print(np.sin(a*1i))


# In[ ]:





# In[ ]:




