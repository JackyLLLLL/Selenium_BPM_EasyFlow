import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.grid(False)

ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])

# 隱藏軸線
plt.axis('off') 
[x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 20 * np.pi - 4*np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
# 調整花瓣邊緣的鋸齒
change = np.sin(15*t)/150
# 調整花瓣開闔的角度，參數可以自己調整
u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2 + change
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))
h = u * (x * np.cos(p) - y * np.sin(p))
# 調整花瓣顏色
c = plt.get_cmap('PuRd')
surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1,
                       cmap= c, linewidth=0, antialiased=True)
plt.show()
