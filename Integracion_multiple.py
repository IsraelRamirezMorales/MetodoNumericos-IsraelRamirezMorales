import numpy as np

# Datos de la tabla
x = np.array([0, 4, 8])  # Valores de x
y = np.array([0, 3, 6])  # Valores de y
T = np.array([            # Matriz de T(x, y)
    [72, 64, 24],         # T(x, y=0)
    [54, 70, 54],         # T(x, y=3)
    [0, 40, 48]           # T(x, y=6)
])

# Regla del trapecio para integrar respecto a x
def integrar_x(T_y, x):
    h = x[1] - x[0]  # Suponemos espaciamiento constante
    return (h / 2) * (T_y[0] + 2 * np.sum(T_y[1:-1]) + T_y[-1])

# Integración para cada y fija
resultados_y = []
for i in range(len(y)):
    resultado_x = integrar_x(T[i, :], x)
    resultados_y.append(resultado_x)

# Regla del trapecio para integrar respecto a y
h_y = y[1] - y[0]  # Suponemos espaciamiento constante en y
resultado_final = (h_y / 2) * (resultados_y[0] + 2 * np.sum(resultados_y[1:-1]) + resultados_y[-1])

print(f"Resultado final de la integral múltiple: {resultado_final} u³")
