import numpy as np
import matplotlib.pylab as plt


datos=np.genfromtxt("datos1.dat")

plt.figure()
plt.title('Datos 1')
plt.plot(datos[:,0],datos[:,1], color='g', label='Sergio was here')
plt.legend()
plt.savefig("plot1.pdf")
