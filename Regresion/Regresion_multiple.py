import numpy as np

def Regresion_multiple():
    # Datos iniciales
    datos_x = np.array([1, 2, 3, 4, 5, 6])
    datos_y = np.array([8,14,25,100,253,492])
    datos_z = np.array([12,50,83,91,104,217])
    lista_auxiliar = []
    tamano = len(datos_x)
        
    suma_x = np.sum(datos_x)
    suma_y = np.sum(datos_y)
    suma_z = np.sum(datos_z)
    print("Suma de x: {} | Suma de y: {}".format(suma_x, suma_y))

    # Configuración de la matriz de sistema y otras variables
    matriz_sistema = [[0] * 3 for _ in range(3)]  # Matriz 3x3 inicializada en ceros
    num_variables = 2  # Número de variables para la matriz

    # Definición de la primera fila
    primera_fila = [[tamano], [datos_y], [datos_x]]
    vector_resultados = [[0] * 1 for _ in range(3)]

    print("Primera fila de variables:", primera_fila)
    continuar = True

    # Ciclo principal para rellenar la matriz
    while continuar:
        for i in range(num_variables + 1):
            vector_resultados[i] = np.sum(calcular_potencias(datos_z, primera_fila[i][0], 1))

            print("Índice actual:", i)
            for j in range(num_variables + 1):
                if i == 0 and j != 0:
                    matriz_sistema[0][j] = np.sum(np.array(primera_fila[j]))
                elif j == 0 and i != 0:
                    matriz_sistema[i][0] = np.sum(np.array(primera_fila[i]))
                else:
                    # Cálculo de elementos en función de la relación de elementos en la matriz
                    if np.array_equal(matriz_sistema[1][j], matriz_sistema[i][1]):
                        matriz_sistema[i][j] = np.sum(calcular_potencias(lista_auxiliar, primera_fila[j][0], 2))
                    else:
                        matriz_sistema[i][j] = np.sum(calcular_potencias(primera_fila[j][0], primera_fila[i][0], 1))

            # Condición de salida del ciclo
            if i == num_variables:
                vector_resultados[0] = np.sum(datos_z)
                matriz_sistema[0][0] = len(datos_x)
                for fila in range(len(matriz_sistema)):
                    for columna in range(len(matriz_sistema)):
                        print("[{}]".format(matriz_sistema[fila][columna]), end='')
                    print()
                print("Vector de resultados:", np.array(vector_resultados))
                solucion = np.linalg.solve(matriz_sistema, np.array(vector_resultados))
                print("Ecuación ajustada: ({}) + ({})x + ({})y".format(solucion[0], solucion[2], solucion[1]))
                continuar = False

    # Retorna la matriz ajustada final
    return matriz_sistema

def calcular_potencias(x, y, exponente):
    x_valido, y_valido = False, False
    x = np.array(x)
    y = np.array(y)
    resultado = 0

    if x.size != 0:
        pot_x = x ** exponente
        resultado = np.sum(pot_x)
        x_valido = True
    if y.size != 0:
        pot_y = y ** exponente
        resultado = np.sum(pot_y)
        y_valido = True
    if x_valido and y_valido:
        producto_xy = x * y
        resultado = np.sum(producto_xy)
        print("x = {} | y = {} | Producto xy = {}".format(x, y, resultado))
    return resultado

Regresion_multiple()
