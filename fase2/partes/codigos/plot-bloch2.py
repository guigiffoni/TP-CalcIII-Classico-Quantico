import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bloch_thermal_cloud(theta0=0, phi0=0, sigma=0.2, N=500):
    """
    Desenha a esfera de Bloch e uma nuvem de pontos perturbados por ruído térmico.
    
    Parâmetros:
        theta0, phi0 : ângulos do estado puro ideal (centro da perturbação)
        sigma        : desvio padrão do ruído (intensidade da temperatura)
        N            : número de pontos na nuvem
    """
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Malha para a esfera unitária (referência)
    u = np.linspace(0, 2*np.pi, 60)
    v = np.linspace(0, np.pi, 60)
    x_sphere = np.outer(np.cos(u), np.sin(v))
    y_sphere = np.outer(np.sin(u), np.sin(v))
    z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_wireframe(x_sphere, y_sphere, z_sphere,
                      color='gray', alpha=0.2, linewidth=0.5)

    # Eixos cartesianos
    for axis, color, label in zip([(1,0,0), (0,1,0), (0,0,1)],
                                  ['r', 'g', 'b'], ['x', 'y', 'z']):
        ax.quiver(0, 0, 0, axis[0], axis[1], axis[2],
                  length=1.0, color=color, alpha=0.6, linewidth=1.5,
                  arrow_length_ratio=0.1)
        ax.text(axis[0]*1.1, axis[1]*1.1, axis[2]*1.1, label, color=color)

    # Polos quânticos
    ax.text(0, 0, 1.1, r'$|0\rangle$', fontsize=14, ha='center')
    ax.text(0, 0, -1.15, r'$|1\rangle$', fontsize=14, ha='center')

    # Vetor do estado puro ideal (sem ruído)
    ideal = np.array([np.sin(theta0)*np.cos(phi0),
                      np.sin(theta0)*np.sin(phi0),
                      np.cos(theta0)])
    ax.quiver(0, 0, 0, ideal[0], ideal[1], ideal[2],
              color='gold', linewidth=3, alpha=0.9, arrow_length_ratio=0.15,
              label='Estado ideal')

    # Gerar pontos perturbados: ruído gaussiano isotrópico
    noise = np.random.normal(0, sigma, (N, 3))
    points = ideal + noise   # nuvem centrada no estado ideal

    # Calcular raios (distância à origem)
    r = np.linalg.norm(points, axis=1)

    # Separar pontos dentro (r <= 1) e fora (r > 1) da esfera
    inside = points[r <= 1]
    outside = points[r > 1]

    # Plotar pontos internos (mistos, decoerência) em azul
    if len(inside) > 0:
        ax.scatter(inside[:,0], inside[:,1], inside[:,2],
                   c='blue', alpha=0.6, s=15, label='Dentro (r<1)')

    # Plotar pontos externos (flutuação térmica) em vermelho
    if len(outside) > 0:
        ax.scatter(outside[:,0], outside[:,1], outside[:,2],
                   c='red', alpha=0.6, s=15, label='Fora (r>1)')

    # Ajustes visuais
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_box_aspect([1,1,1])
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.grid(False)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Bloch térmico – σ = {sigma}', fontsize=14)
    ax.legend(loc='upper right')

    plt.show()

# ========== EXEMPLO DE USO ==========
if __name__ == "__main__":
    # Estado ideal: |+⟩ = (|0⟩+|1⟩)/√2  -> theta = pi/2, phi = 0
    bloch_thermal_cloud(theta0=np.pi/2, phi0=0, sigma=0.25, N=600)