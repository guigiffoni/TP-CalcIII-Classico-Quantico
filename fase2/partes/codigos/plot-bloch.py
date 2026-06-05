import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Esfera de Bloch (O recipiente sólido e fosco)
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:20j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_surface(x, y, z, color='royalblue', alpha=0.15, shade=True)
ax.plot_wireframe(x, y, z, color="royalblue", alpha=0.2, linewidth=0.5)

# 2. Nuvem de Incerteza (O erro)
rT = 0.2752
n_pontos = 1000
phi = np.random.uniform(0, 2*np.pi, n_pontos)
costheta = np.random.uniform(-1, 1, n_pontos)
u = np.random.uniform(0, 1, n_pontos)
theta = np.arccos(costheta)
r = rT * u**(1/3)
x_n = r * np.sin(theta) * np.cos(phi)
y_n = r * np.sin(theta) * np.sin(phi)
z_n = r * np.cos(theta) + 1 
ax.scatter(x_n, y_n, z_n, color='orange', alpha=0.4, s=2)

ax.set_box_aspect([1,1,1]); ax.view_init(elev=20, azim=45)
plt.show()