import numpy as np
import matplotlib.pyplot as plt

def calc_P(T):
    r = 0.5 * (T - 25) / 75
    return r**3 * 100

T = np.linspace(25, 100, 500)
P = calc_P(T)

fig, ax = plt.subplots(figsize=(7, 4))

# zonas
ax.axvspan(25, 40, color='#E1F5EE', alpha=0.85)
ax.axvspan(40, 56, color='#FAEEDA', alpha=0.85)
ax.axvspan(56, 100, color='#FCEBEB', alpha=0.85)
ax.axvline(x=40, color='#888780', linewidth=0.5, linestyle='--')
ax.axvline(x=56, color='#888780', linewidth=0.5, linestyle='--')

# rótulos das zonas
ax.text(32.5, 4.6, 'Seguro',  fontsize=9, color='#0F6E56', ha='center', fontweight='bold')
ax.text(48.0, 4.6, 'Atenção', fontsize=9, color='#854F0B', ha='center', fontweight='bold')
ax.text(78.0, 4.6, 'Falha',   fontsize=9, color='#A32D2D', ha='center', fontweight='bold')

# curva (limitada a P <= 5%)
mask = P <= 5
ax.plot(T[mask], P[mask], color='#534AB7', linewidth=2.5, zorder=5)

# indicador de saída do gráfico
ax.annotate('', xy=(80.26, 5.0), xytext=(80.26, 4.5),
            arrowprops=dict(arrowstyle='->', color='#A32D2D', lw=1.5))
ax.text(80.8, 4.72, '12,5% em\n100°C', fontsize=7.5, color='#A32D2D', va='center')

# linhas tracejadas do resultado atual
T_cur, P_cur = 66.28, 2.08
ax.plot([T_cur, T_cur], [0, P_cur], color='#BA7517', lw=1, ls='--', alpha=0.7)
ax.plot([25,    T_cur], [P_cur, P_cur], color='#BA7517', lw=1, ls='--', alpha=0.7)

# ponto e rótulo do resultado atual
ax.scatter([T_cur], [P_cur], color='#854F0B', s=60, zorder=6)
ax.annotate('T = 66,28°C\nP = 2,08%',
            xy=(T_cur, P_cur), xytext=(T_cur + 1.5, P_cur + 0.45),
            fontsize=8.5, color='#633806', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FAEEDA',
                      edgecolor='#BA7517', linewidth=0.5))

# ponto T=56°C
T_56 = 56.0
P_56 = calc_P(T_56)
ax.scatter([T_56], [P_56], color='#854F0B', s=30, zorder=6)
ax.text(T_56 + 1, P_56 - 0.18, f'56°C → {P_56:.2f}%', fontsize=8.5, color='#854F0B')

# seta −10°C
mid_y = (P_cur + P_56) / 2
ax.annotate('', xy=(T_56 + 1, mid_y), xytext=(T_cur - 1, mid_y),
            arrowprops=dict(arrowstyle='->', color='#0F6E56', lw=1.5))
ax.text((T_cur + T_56) / 2, mid_y + 0.14, '−10°C',
        fontsize=9, color='#0F6E56', ha='center')

# eixos
ax.set_xlim(25, 100)
ax.set_ylim(0, 5)
ax.set_xlabel('Temperatura média do chip (°C)', fontsize=11)
ax.set_ylabel(r'$P_{erro}$ (%)', fontsize=11)
ax.set_xticks([25, 40, 56, 66, 80, 100])
ax.set_xticklabels(['25°C','40°C','56°C','66°C','80°C','100°C'])
ax.set_yticks([0, 1, 2, 3, 4, 5])
ax.set_yticklabels(['0%','1%','2%','3%','4%','5%'])
ax.grid(axis='y', alpha=0.25, linewidth=0.5)

plt.tight_layout()
plt.savefig('../../img/curva-perro-temperatura.pdf', bbox_inches='tight')
plt.savefig('../../img/curva-perro-temperatura.png', bbox_inches='tight', dpi=150)
print("Salvo em fase2/img/")