import numpy as np
from scipy.linalg import solve

def Interpolacion_Segmentada():
    # Datos de entrada
    x = np.array([3, 4.5, 7, 9])
    y = np.array([2.5, 1, 2.5, 0.5])

    # Definimos los intervalos
    n = len(x) - 1  # Número de intervalos
    a = np.zeros(n)  # Coeficiente a_i
    b = np.zeros(n)  # Coeficiente b_i
    c = np.zeros(n + 1)  # Coeficiente c_i, tamaño n+1

    # Coeficiente a_i es simplemente y_i
    for i in range(n):
        a[i] = y[i]

    # Crear el sistema de ecuaciones para los coeficientes c
    if n > 1:  # Verificamos que hay más de un intervalo
        A = np.zeros((n - 1, n - 1))  # Matriz del sistema
        B = np.zeros(n - 1)            # Término independiente

        # Condiciones de continuidad de la primera derivada
        for i in range(1, n):
            A[i - 1, i - 1] = 2 * (x[i + 1] - x[i - 1])
            if i < n - 1:
                A[i - 1, i] = x[i + 1] - x[i]
                A[i, i - 1] = x[i] - x[i - 1]
            
            B[i - 1] = 6 * ((y[i + 1] - y[i]) / (x[i + 1] - x[i]) - (y[i] - y[i - 1]) / (x[i] - x[i - 1]))

        # Resolver el sistema para obtener los coeficientes c
        c[1:n] = solve(A, B)

    # Calcular los coeficientes b_i
    for i in range(n):
        b[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i]) - (x[i + 1] - x[i]) * (2 * c[i] + c[i + 1]) / 6

    # Mostrar las funciones splines cuadráticas
    for i in range(n):
        spline_func = f"S{i}(x) = {a[i]} + {b[i]:.4f}(x - {x[i]}) + {c[i]:.4f}(x - {x[i]})^2"
        print(spline_func)

    # Evaluar en x_valor = 5
    x_valor = 5
    # Determinar el intervalo donde cae x_valor
    for i in range(n):
        if x[i] <= x_valor <= x[i + 1]:
            f_x = a[i] + b[i] * (x_valor - x[i]) + c[i] * (x_valor - x[i]) ** 2
            print(f"\nf({x_valor}) = {f_x:.4f} en el intervalo [{x[i]}, {x[i + 1]}]")
            break 

# Llamar a la función
Interpolacion_Segmentada()
