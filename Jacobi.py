import numpy as np
import sympy as sp
import math
from Utils.Errores import Errores
from Utils.Asks import Asks
from Utils.Cifras_significativas import Cifras_significativas

def generar_matriz(numero_columnas): 
    matriz = np.array([3])
    if numero_columnas != 1:
        columna_nueva = np.array([3])
        for i in range(numero_columnas - 1):
            matriz = np.hstack((matriz, columna_nueva))
    return matriz    

def Jacobi(n):
    # Inicializo los errores, cifras significativas
    cifras_significativas = Cifras_significativas()
    errores = Errores()
    soluciones = []
    matriz = np.empty((0,0))

    A = np.array([[3, -1, -1], 
                  [-1, 3, 1], 
                  [2, 1, 4]])
    B = np.array([1, 3, 7])  # Igualdad de la matriz

    # Imprimir el sistema de ecuaciones 
    print("\nSistema de ecuaciones:")
    for i in range(len(B)):
        equation = " + ".join([f"{A[i, j]} * x_{j + 1}" for j in range(len(A[i]))])
        print(f"{equation} = {B[i]}")

    # Cambiar el valor inicial de las variables
    x_i = np.array([0,0,0])#1.529, 1.9412, 4.471
    D = np.diag(np.diag(A))
    D_inv = np.linalg.inv(D)
    Tx = D - A
    T = np.dot(D_inv, Tx)
    C = np.dot(D_inv, B)

    # Variables para iteraciones
    row = 1
    error_tolerable = errores.calcular_error_tolerable(n)

    # Cabecera de la tabla
    print("\nIteraciones del método de Jacobi:")
    print(f"{'i':<5}{'x1':<15}{'x2':<15}{'x3':<15}{'Error relativo'}")
    
    # Ciclo de iteración para Jacobi
    while True:
        # Calcular valor nuevo para las variables
        x_j = cifras_significativas.vector_cifras_significativas(np.dot(T, x_i), n) + cifras_significativas.vector_cifras_significativas(C, n)
        x_j = cifras_significativas.vector_cifras_significativas(x_j, n)

        # Calcular los errores relativos 
        errores_relativos = errores.calcular_errores_relativos(x_i, x_j, n)

        # Imprimir los valores de la iteración actual
        print(f"{row:<5}{x_j[0]:<15}{x_j[1]:<15}{x_j[2]:<15}{errores_relativos}")

        # Comprobar si todos los errores relativos están por debajo del error tolerable
        if all(error < error_tolerable for error in errores_relativos):
            soluciones = x_j
            break

        # Actualizar el valor de las variables para la siguiente iteración
        x_i = x_j
        row += 1

    return [matriz, soluciones]

def main():
    print("-------------------METODO JACOBI-------------------")
    asks = Asks()

    while True:
        n = asks.ask_for_int("¿Con cuántas cifras significativas desea trabajar?")
        if n < 1:
            print("El mínimo de cifras significativas es 1, inténtalo de nuevo")
        else:
            break

    array = Jacobi(n)
    soluciones = array[1]

    print(f"\nSOLUCIONES:")
    for i in range(len(soluciones)):
        print(f"X_{i + 1}: {soluciones[i]}")
    
if __name__ == "__main__":
    main()
