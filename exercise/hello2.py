from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import math
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import rc
mpl.rcParams['figure.dpi'] = 350

# Display the mesh
fig = plt.figure()
ax = fig.gca(projection='3d')               # to work in 3d

# Generate torus mesh
limit = 32 * 2
angle = np.linspace(0, 2 * np.pi, limit)
theta, phi = np.meshgrid(angle, angle)

r, R = .2, 1.
sX = (R + r * np.cos(phi)) * np.cos(theta)
sY = (R + r * np.cos(phi)) * np.sin(theta)
sZ = r * np.sin(phi)

#ax.plot_surface(sX, sY, sZ, color = 'w', rstride = 1, cstride = 1)

r, R = .3, 1
sX = (R + r * np.cos(phi)) * np.cos(theta)
sY = (R + r * np.cos(phi)) * np.sin(theta)
sZ = r * np.sin(phi)

step = 1
for i in range (0,limit):
    for j in range (0, limit):
        ax.scatter3D(sX[i:i+step,j:j+step], sY[i:i+step,j:j+step], sZ[i:i+step,j:j+step], color = "C2", s = 1)
        
#ax.plot_wireframe(sX, sY, sZ, color = 'w', rstride = 1, cstride = 1, linewidth = 1)
            
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.set_zlabel('$Z$')

ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_zlim(-1, 1)

plt.show()