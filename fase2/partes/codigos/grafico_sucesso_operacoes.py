import numpy as np
import matplotlib.pyplot as plt

# Probabilidade de erro calculada no trabalho
P_erro = 0.0208

# Número de operações
d = np.arange(0, 1001)

# Probabilidade de sucesso acumulada
P_sucesso = ((1 - P_erro) ** d) * 100

plt.figure(figsize=(9, 5))

plt.plot(
    d,
    P_sucesso,
    linewidth=2
)

# Pontos da Tabela 2
operacoes = [10, 100, 1000]
sucesso_tabela = [81, 12, 0.00000001]

plt.scatter(
    operacoes,
    sucesso_tabela,
    s=40,
    label="Valores da Tabela 2"
)

plt.title("Probabilidade de sucesso em função do número de operações")
plt.xlabel("Número de operações")
plt.ylabel("Probabilidade de sucesso (%)")

plt.grid(True)
plt.legend()

plt.savefig(
    "grafico_sucesso_operacoes.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()