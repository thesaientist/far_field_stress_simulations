# Python script to explore exponential pressure pulse decay for HEGF

# Initial setup
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

""" PRESSURE PULSE PARAMETERS """
P0 = 100                          # Pressure pulse peak pressure (MPa)
t0 = 1.0e-2                         # Pressure rise time (s)
#alpha = 5000                           # Decay parameter (/s)
ratio = 1.5                         # Beta/alpha ratio (decay parameters)

# anonymous function that beta value needs to satisfy to fit pressure pulse shape
func = lambda alpha : ratio*alpha - alpha*np.exp((ratio-1)*alpha*t0)

""" PLOT THE ABOVE FUNCTION TO GET INITIAL GUESS FOR BETA"""
alpha = np.linspace(0,100,200)

fig1 = plt.figure()
plt.plot(alpha,func(alpha))
plt.xlabel('alpha')
plt.ylabel('transcendental expression')
plt.grid()
plt.show()

""" SOLVE FOR BETA VALUE USING SCIPY FSOLVE """
alpha0 = 90
alpha_sol = fsolve(func, alpha0)
print "Alpha value: %f" %(alpha_sol)
beta = ratio*alpha_sol
print "Beta value: %f" %(beta)

""" DETERMINE ARRAYS FOR TIME AND PRESSURE/STRESS """
t = np.linspace(0,0.05,num=500)
P = P0*(np.exp(-alpha_sol*t)-np.exp(-beta*t))/(np.exp(-alpha_sol*t0)-np.exp(-beta*t0))

# np.savetxt('xxxxx.txt',node_array,fmt=['%8.8f','%8.8f','%8.8f','%i','%8.8f'],delimiter='  ')

""" PLOT USING MATPLOTLIB """
fig2 = plt.figure()
#plt.rc('text',usetex=True)
#plt.rc('font',family='serif')
plt.plot(t,P,'r-o')
plt.xlabel('Time (sec)')
plt.ylabel('Stress (MPa)')
plt.title('Pulse Pressurization of Borehole')
plt.axis([0,0.05,0,200])
plt.grid()
plt.show()
