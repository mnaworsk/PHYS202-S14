
import numpy as np

def trapz(func, a, b, N): 
    """this function claculates an integral by approximating the area with
    trapezoidal pieces""" 
    h = (b-a)/N
    
    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())
    return I

def simps(func, a, b, N): 
    """this function calculates an integral with quadratic curves. 
    It is a closer approximation that the trapezoidal rule."""
    h = (b-a)/N
    
    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    I = I = (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())
    
    return I