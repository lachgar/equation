import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
import numpy as np
from matplotlib.ticker import FuncFormatter, MultipleLocator

def f(o1, o2, m1, m2, ro ):
    return m1 * ro * np.cos(o1) + m2 * ro * np.cos(o2);

o1 = np.linspace(-np.pi, np.pi, 30)
o2 = np.linspace(-np.pi, np.pi, 30)
X, Y = np.meshgrid(o1, o2)
# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))
fig.suptitle('m1 * ro * np.cos(o1) + m2 * ro * np.cos(o2)', fontsize=16)

#===============
#  First subplot
#===============
# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')
Z = f(X, Y, 1, 1, np.pi/2)
ax.xaxis.set_major_formatter(FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))
ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))
ax.yaxis.set_major_formatter(FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))
ax.yaxis.set_major_locator(MultipleLocator(base=np.pi))
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=10)
ax.set_title('m1 = 1; m2 = 1; ro=1/2$\pi$');
ax.set_xlabel('o1')
ax.set_ylabel('o2')
ax.set_zlabel('f');
#===============
# Second subplot
#===============
# set up the axes for the second plot
ax = fig.add_subplot(1, 2, 2, projection='3d')
Z = f(X, Y, 10, -10, np.pi/2)
ax.xaxis.set_major_formatter(FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))
ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))
ax.yaxis.set_major_formatter(FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))
ax.yaxis.set_major_locator(MultipleLocator(base=np.pi))
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=10)
ax.set_title('m1 = 10; m2 = -10; ro=1/2$\pi$');
ax.set_xlabel('o1')
ax.set_ylabel('o2')
ax.set_zlabel('f')
plt.show()
