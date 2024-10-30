import numpy as np

# Datos iniciales
x_values = [6, 8, 10, 12]  # Valores de x conocidos
y_values = [9, 25, 55, 105]  # Valores de f(x) conocidos

# Número de puntos
n = len(y_values)

# Crear una tabla de diferencias hacia atrás
diferencias = np.zeros((n, n))
diferencias[:, 0] = y_values

# Calculamos las diferencias hacia atrás
for j in range(1, n):
    for i in range(j, n):
        diferencias[i][j] = diferencias[i][j - 1] - diferencias[i - 1][j - 1]

# Mostrar la tabla de diferencias hacia atrás
print("Tabla de diferencias hacia atrás:")
for row in diferencias:
    print(row)

# Parámetros iniciales para la interpolación
x_n = x_values[-1]   # Último valor de x conocido
h = x_values[1] - x_values[0]   # Asumimos intervalos uniformes
x_interpolar = 11   # Valor en el que queremos estimar f(x)
k = (x_interpolar - x_n) / h   # Valor de k (diferencia relativa de x respecto a x_n)

# Interpolación usando el método de Newton hacia atrás
y_interpolado = diferencias[-1, 0]  # Primer término del polinomio hacia atrás (última y conocida)
factorial = 1   # Para almacenar el factorial de cada término

# Iteración para construir el polinomio de Newton hacia atrás
for i in range(1, n):
    # Cálculo del producto acumulado de k(k+1)(k+2)...(k+i-1)
    k_product = k
    for j in range(1, i):
        k_product *= (k + j)

    # Actualización del factorial
    factorial *= i

    # Sumar término correspondiente al polinomio de Newton hacia atrás
    y_interpolado += (k_product / factorial) * diferencias[n - 1, i]

# Resultado de la interpolación
print(f"El valor interpolado de f({x_interpolar}) es aproximadamente: {y_interpolado:.4f}")
