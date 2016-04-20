# Determine an asymptotic function to apply to the displacement BC and have a time dependence on in-situ stress application

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

a = 100                          # time factor for asymptotic function
t = np.linspace(0,5.0e-2,num=20)
y = 1-np.exp(-a*t)

# Plot
fig1 = plt.figure()
plt.plot(t,y,'r-o')
plt.xlabel('Time (sec)')
plt.ylabel('Scaling Factor')
#plt.title('Pulse Pressurization of Borehole')
plt.xlim([0,t[-1]])
plt.grid()
plt.show()

print y[-1]
