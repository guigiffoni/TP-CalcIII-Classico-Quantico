from scipy.integrate import tplquad
import numpy as np

rT = 0.2752
def integrando(theta, phi, rho):
    return rho**2 * np.sin(phi)

V_inc, _ = tplquad(
    integrando, 0, rT, 
    lambda r: 0, lambda r: np.pi, lambda r, p: 0, lambda r, 
    p: 2*np.pi
)

print(f'V_inc = {V_inc:.5f}')  # -> 0.08741