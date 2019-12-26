import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cmath #for complex number operations
 
##TARGET: plot the following functions
#exp(j*theta)
#cos(theta) + j*sin(theta)

### MODELING: ---< A*sin(w*t + theta) == A*sin(w*t) , where w =2*pi*f, t is time >
## VARIABLES
# t <----- boundary times [0, T]
# f = constant
# w*t = 2*pi*f * t
# sin(w*t)
A = 4                             #GAIN FACTOR
t = np.arange(0,10,.01)           #TIME RANGE (0,T) 
f = .5                            #FREQUENCY, Hz 
siny = A * np.sin(2*np.pi*f * t)  #Y = SIN(t)
cosy = A * np.cos(2*np.pi*f * t)  #Y = SIN(t)
plt.plot(siny,cosy)               #PLOT 2D
#-----END ---A*sin(w*t) > 

##--< plot3D >
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(t, siny, cosy, label="$Ae^{j\u03C9t}$ = $A[cos(\u03C9t) + jsin(\u03C9t)]$ \nwhere, $\u03C9 = 2\u03C0f$")
ax.legend()
ax.grid(False)

#ax.set_axis_off()
ax.set_xlabel('time (t)')
ax.set_ylabel('Imaginary axis (j)')
ax.set_zlabel('Amplitude (A)')
plt.show()
fig.savefig('plot.png')

##------END-- < sin( >