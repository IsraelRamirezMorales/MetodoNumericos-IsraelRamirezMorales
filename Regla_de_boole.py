import numpy as np

# Definición de la función a integrar
def f(x):
    return np.exp(x**4)

# Parámetros de la integral
a = -1  # Límite inferior
b = 1  # Límite superior
n = 8  # Número de segmentos (para la regla de Boole, debe ser múltiplo de 4)

# Paso de discretización
h = (b - a) / n

# Valores de x
x_values = np.linspace(a, b, n + 1)

# Evaluación de la función en los puntos x
f_values = f(x_values)

# Aplicación de la Regla de Boole
I = (b - a) / 90 * (7 * f_values[0] + 32 * f_values[1] + 12 * f_values[2] + 32 * f_values[3] + 7 * f_values[4])

print("El valor de la integral es:", I)