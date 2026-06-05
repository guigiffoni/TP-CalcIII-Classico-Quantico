import numpy as np
import matplotlib.pyplot as plt

# Discretização (os mesmos dados do roteiro)
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
T = 60 + 100 * np.exp(-((X-0.5)**2 + (Y-0.5)**2) / 0.02)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, T, cmap='hot', edgecolor='none', alpha=0.9)
ax.set_title('Hotspot Gaussiano no Processador')
ax.set_zlim(50, 170)
plt.colorbar(surf, label='Temperatura (°C)')
plt.show()