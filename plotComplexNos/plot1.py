import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cmath #for complex number operations
 
"""
cnums = np.arange(5) + 1j * np.arange(6,11)
X = [x.real for x in cnums]
Y = [x.imag for x in cnums]
plt.scatter(X,Y, color='red')
plt.show()"""

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

ax.plot(t, siny, cosy, label="$e^{j\u03C9t}$ = cos(\u03C9t) + jsin(\u03C9t); \nwhere, \u03C9 = 2\u03C0f")
ax.legend()
ax.grid(False)

#ax.set_axis_off()
ax.set_xlabel('time')
ax.set_ylabel('Imaginary axis')
ax.set_zlabel('Amplitude')
plt.show()
fig.savefig('plot.png')

##------END-- < sin( >

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

"""
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
"""




x = np.arange(0,4*np.pi,0.1)   # one period sine wave (0,4*pi)

##sin(theta), cos...
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
plt.plot(x,y)

np.sin(2*np.pi*10)

##COMPLEX NUMBER
a=np.sin(x)
b=np.cos(x)
zA = a+1j*b   #--< creating array of complex numbers >
##


np.arange(len(a)) + 1j * np.arange(6,11)

for ix in range(len(a)):
    #ix+=1
    
print(ix)
z=complex(a,b)
for i
z= complex(np.sin(x),np.cos(x))

cnums = np.arange(5) + 1j * np.arange(6,11)
cnums = np.exp()
X = [x.real for x in cnums]
Y = [x.imag for x in cnums]
plt.scatter(X,Y, color='red')
plt.show()



# Python code to demonstrate the working of 
# complex(), real() and imag() 
  
# importing "cmath" for complex number operations 
  
# Initializing real numbers 
x = 5
y = 3
# converting x and y into complex number 
z = complex(x,y); 
  
# printing real and imaginary part of complex number 
print ("The real part of complex number is : ",end="") 
print (z.real) 
  
print ("The imaginary part of complex number is : ",end="") 
print (z.imag) 








#https://pythonforundergradengineers.com/plotting-sin-cos-with-matplotlib.html
