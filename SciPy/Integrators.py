
def trapz(func, a, b, n): 
    """this function claculates an integral by approximating the area with
    trapezoidal pieces""" 
    a = 0.0
    b = 2.0
    h = (b-a)/N
    
    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())

def simps(func, a, b, n): 
    """this function calculates an integral with quadratic curves. 
    It is a closer approximation that the trapezoidal rule."""
    a = 0.0
    b = 2.0
    h = (b-a)/N

    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)


print file.name