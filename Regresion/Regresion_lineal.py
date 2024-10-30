import numpy as np
import math

def regresion_lineal():
    valores_x = np.array([1, 2, 3, 4, 5, 6])    
    valores_y = np.array([8,14,25,100,253,492])
    error, suma_xy, suma_x_var, suma_y_var = 0, 0, 0, 0
    suma_x = np.sum(valores_x)
    suma_y = np.sum(valores_y)
    productos_xy = valores_x * valores_y
    suma_productos_xy = np.sum(productos_xy)
    cuadrados_x = [valor ** 2 for valor in valores_x]
    suma_cuadrados_x = np.sum(cuadrados_x)

    coeficiente_a1 = ((len(valores_x) * suma_productos_xy) - (suma_x * suma_y)) / ((len(valores_x) * suma_cuadrados_x) - (suma_x) ** 2)
    coeficiente_a0 = (suma_y / len(valores_x)) - (coeficiente_a1 * (suma_x / len(valores_x)))

    print("Coeficiente a1 = {}".format(coeficiente_a1))
    print("Coeficiente a0 = {}".format(coeficiente_a0))

    for i in range(len(valores_x)):
        error = round(((valores_y[i] - coeficiente_a0 - (coeficiente_a1 * valores_x[i])) ** 2) + error, 4)
        print("Error en punto {}: {} - {} - {} * {} = {}".format(i+1, valores_y[i], coeficiente_a0, coeficiente_a1, valores_x[i], error))

    print("Ecuación ajustada: y = {} + {}x ± {}".format(coeficiente_a0, coeficiente_a1, error))
    valor_y_estimado = coeficiente_a0 + (coeficiente_a1 * len(valores_x)) - error

    for i in range(len(valores_x)):
        suma_xy = ((valores_x[i] - (suma_x / len(valores_x))) * (valores_y[i] - (suma_y / len(valores_x)))) + suma_xy
        suma_x_var = (valores_x[i] - (suma_x / len(valores_x))) ** 2 + suma_x_var
        suma_y_var = (valores_y[i] - (suma_y / len(valores_x))) ** 2 + suma_y_var

    coeficiente_r = suma_xy / (np.sqrt(suma_x_var) * np.sqrt(suma_y_var))
    print("Coeficiente de correlación R = {}".format(coeficiente_r))

# Ejemplo de uso
regresion_lineal()
