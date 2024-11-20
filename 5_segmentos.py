import numpy as np

def f(x):
    return x**2+3*x-9

a = 0  # Límite inferior
b = 4  # Límite superior
n = 5  # Número de segmentos (deben ser 5)

# Paso
h = (b - a) / n

# Valores de x
x_values = np.linspace(a, b, n + 1)

# Evaluación de la función en los puntos x
f_values = f(x_values)


I = (b - a) / 288 * (19* f_values[0] + 75 * f_values[1] + 50 * f_values[2] + 50 * f_values[3] + 75 * f_values[4] + 19 * f_values[5])

print("El valor de la integral es:", I)