import numpy as np
import matplotlib.pylab as plt


datos=np.genfromtxt("datos.dat")

plt.figure()
plt.title('Datos')
plt.plot(datos[:,0],datos[:,1], color='r')
plt.savefig("plot.pdf")
