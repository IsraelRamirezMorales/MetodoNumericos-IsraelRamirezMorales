import numpy as np
import math

def Interpolacion_Inversa():
    puntos_x = np.array([1, 2, 3, 4, 5])    
    puntos_y = np.array([1, 0.5, 0.3333, 0.25, 0.2])
    
    valor_objetivo = 10 / 3
    funcion_str = "1/x"
    funcion_evaluada = eval("lambda x: " + funcion_str)

    resultado_evaluado = funcion_evaluada(valor_objetivo)
    indice_cercano = buscar_valor_cercano(puntos_y, resultado_evaluado)
    puntos_x_cercanos = np.array([puntos_x[indice_cercano - 1], puntos_x[indice_cercano], puntos_x[indice_cercano + 1]])
    puntos_y_cercanos = np.array([puntos_y[indice_cercano - 1], puntos_y[indice_cercano], puntos_y[indice_cercano + 1]])
    
    print("Puntos x seleccionados:", puntos_x_cercanos)
    print("Puntos y seleccionados:", puntos_y_cercanos)
    
    coeficientes = calcular_coeficientes_interpolacion(puntos_x_cercanos, puntos_y_cercanos)
    print("Coeficientes del polinomio:", coeficientes)
    print("Resultado evaluado:", resultado_evaluado)
    
    raiz_positiva = (-(coeficientes[1]) + np.sqrt(coeficientes[1]**2 - 4 * coeficientes[2] * (coeficientes[0] - resultado_evaluado))) / (2 * coeficientes[2])
    raiz_negativa = (-(coeficientes[1]) - np.sqrt(coeficientes[1]**2 - 4 * coeficientes[2] * (coeficientes[0] - resultado_evaluado))) / (2 * coeficientes[2])
    print("Ecuación cuadrática:", "-{} + sqrt({}^2 - 4 * {} * ({} - {})) / (2 * {})".format(coeficientes[1], coeficientes[1], coeficientes[2], coeficientes[0], resultado_evaluado, coeficientes[2]))
    print("Raíces obtenidas: raíz positiva = {}, raíz negativa = {}".format(raiz_positiva, raiz_negativa))

    return raiz_positiva

def calcular_coeficientes_interpolacion(puntos_x, puntos_y):
    tamano = len(puntos_x)
    matriz_vandermonde = np.zeros((tamano, tamano), dtype=float)
    for fila in range(tamano):
        for columna in range(tamano):
            matriz_vandermonde[fila, columna] = puntos_x[fila] ** columna

    if np.linalg.det(matriz_vandermonde) != 0:
        solucion_matriz = np.linalg.solve(matriz_vandermonde, puntos_y)
    else:
        print("Error: La matriz no tiene inversa (determinante es 0).")

    return solucion_matriz

def buscar_valor_cercano(puntos_y, resultado):
    diferencia_minima = abs(resultado - puntos_y[0])
    indice_mas_cercano = 0

    for i in range(len(puntos_y)):
        if abs(resultado - puntos_y[i]) < diferencia_minima:
            diferencia_minima = abs(resultado - puntos_y[i])
            indice_mas_cercano = i

    return indice_mas_cercano

Interpolacion_Inversa()
