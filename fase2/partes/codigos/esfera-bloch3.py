import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros do trabalho
rT = 0.2752  # raio da nuvem de incerteza térmica
np.random.seed(42)

fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Esfera de Bloch (superfície wireframe) ---
u = np.linspace(0, 2 * np.pi, 60)
v = np.linspace(0, np.pi, 40)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(xs, ys, zs, color='lightblue', alpha=0.08, linewidth=0)
ax.plot_wireframe(xs, ys, zs, color='steelblue', alpha=0.15, linewidth=0.4)

# --- Estado ideal: pontos NA superfície (r = 1) ---
n_surface = 80
phi_s = np.random.uniform(0, np.pi, n_surface)
theta_s = np.random.uniform(0, 2 * np.pi, n_surface)
x_s = np.sin(phi_s) * np.cos(theta_s)
y_s = np.sin(phi_s) * np.sin(theta_s)
z_s = np.cos(phi_s)
ax.scatter(x_s, y_s, z_s, color='limegreen', s=12, alpha=0.7,
           label='Estado puro (r = 1, sem ruído)', zorder=5)

# --- Estado misto: pontos DENTRO da esfera de raio rT (r < rT) ---
n_mixed = 120
# Amostragem uniforme dentro de uma esfera de raio rT
r_m = rT * (np.random.uniform(0, 1, n_mixed) ** (1/3))
phi_m = np.random.uniform(0, np.pi, n_mixed)
theta_m = np.random.uniform(0, 2 * np.pi, n_mixed)
x_m = r_m * np.sin(phi_m) * np.cos(theta_m)
y_m = r_m * np.sin(phi_m) * np.sin(theta_m)
z_m = r_m * np.cos(phi_m)
ax.scatter(x_m, y_m, z_m, color='tomato', s=14, alpha=0.75,
           label=f'Estado misto; nuvem térmica (r ≤ rT = {rT})', zorder=5)

# --- Eixos ---
ax.quiver(0, 0, -1.4, 0, 0, 2.8, color='gray', arrow_length_ratio=0.05,
          linewidth=0.8, alpha=0.5)
ax.quiver(-1.4, 0, 0, 2.8, 0, 0, color='gray', arrow_length_ratio=0.05,
          linewidth=0.8, alpha=0.5)
ax.quiver(0, -1.4, 0, 0, 2.8, 0, color='gray', arrow_length_ratio=0.05,
          linewidth=0.8, alpha=0.5)

# --- Rótulos dos polos ---
ax.text(0, 0, 1.15, r'$|0\rangle$', fontsize=13, ha='center', color='navy', fontweight='bold')
ax.text(0, 0, -1.22, r'$|1\rangle$', fontsize=13, ha='center', color='navy', fontweight='bold')
ax.text(1.18, 0, 0, r'$|+\rangle$', fontsize=11, ha='center', color='gray')
ax.text(0, 1.18, 0, r'$|i\rangle$', fontsize=11, ha='center', color='gray')

# --- Indicador do raio rT ---
ax.quiver(0, 0, 0, 0, rT, 0, color='darkred', arrow_length_ratio=0.15,
          linewidth=1.5, label=f'rT = {rT}')
ax.text(0.04, rT/2, 0.03, f'rT = {rT}', fontsize=9, color='darkred')

# --- Esferinha de incerteza (contorno) ---
u2 = np.linspace(0, 2 * np.pi, 40)
v2 = np.linspace(0, np.pi, 30)
xi = rT * np.outer(np.cos(u2), np.sin(v2))
yi = rT * np.outer(np.sin(u2), np.sin(v2))
zi = rT * np.outer(np.ones(np.size(u2)), np.cos(v2))
ax.plot_wireframe(xi, yi, zi, color='darkred', alpha=0.25, linewidth=0.5)

# --- Formatação ---
ax.set_xlim([-1.4, 1.4])
ax.set_ylim([-1.4, 1.4])
ax.set_zlim([-1.4, 1.4])
ax.set_box_aspect([1, 1, 1])
ax.set_axis_off()

ax.set_title(f'Esfera de Bloch; Decoerência Térmica\n'
             f'Volume de incerteza: Vinc ≈ 0.0874  |  Perro ≈ 2.08%',
             fontsize=12, fontweight='bold', pad=12)

legend = ax.legend(loc='upper left', fontsize=9, framealpha=0.85,
                   bbox_to_anchor=(-0.05, 1.0))

ax.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()