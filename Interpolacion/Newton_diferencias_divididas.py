import numpy as np

def diferencias_divididas(x, y):
    n = len(y)
    # Crear una tabla de diferencias divididas
    diferencias = np.zeros((n, n))
    diferencias[:, 0] = y  # Coloca los valores de y en la primera columna

    # Calcular la tabla de diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            diferencias[i][j] = (diferencias[i + 1][j - 1] - diferencias[i][j - 1]) / (x[i + j] - x[i])

    return diferencias

def polinomio_newton(x_values, y_values, x):
    n = len(x_values)
    diferencias = diferencias_divididas(x_values, y_values)

    # El polinomio de Newton empieza con el primer término
    resultado = diferencias[0][0]

    # Cálculo de p
    p = 1  # Comenzamos con p = 1 (corresponde a (x - x_0))
    
    # Sumar los términos del polinomio
    for i in range(1, n):
        p *= (x - x_values[i - 1])  # Actualizamos p
        resultado += p * diferencias[0][i]  # Añadimos el término correspondiente

    return resultado

# Ejemplo de uso con tus valores
x_values = [6, 8, 10, 12]  # Valores x conocidos
y_values = [9, 25, 55, 105]  # Valores y conocidos

# Valor en el que se quiere estimar f(x)
x_deseada = 11
resultado = polinomio_newton(x_values, y_values, x_deseada)
print(f"El valor estimado de f({x_deseada}) es: {resultado:.4f}")