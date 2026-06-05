from scipy.integrate import dblquad
import numpy as np

def T(y, x):
    return 60 + 100*np.exp(-((x-0.5)**2 + (y-0.5)**2) / 0.02)

resultado, erro = dblquad(T, 0, 1, lambda x: 0, lambda x: 1)

print(f'T_media = {resultado:.4f} C')   # -> 66.2832 C
print(f'Erro estimado = {erro:.2e}')    # -> 3.5e-10