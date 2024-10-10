import numpy as np
import sympy as sp
import math
from Utils.Errores import Errores
from Utils.Asks import Asks
from Utils.Cifras_significativas import Cifras_significativas
from Utils.Operaciones.Operaciones_newton_raphson import Operaciones_newton_raphson

def generar_matriz(numero_columnas):
    matriz = np.array([3])
    if numero_columnas != 1:
        new_column = np.array([3])
        for i in range(numero_columnas - 1):
            matriz = np.hstack((matriz, new_column))
    return matriz   

def Newton_raphson(n):
    #Inicializo los errores, cifras significativas, operaciones del metodo
    errores=Errores()
    operaciones=Operaciones_newton_raphson()
    cifras_significativas=Cifras_significativas()
    x, y, z = sp.symbols('x y z')  
    soluciones = []
    matriz = np.empty((0,0))
    
    A = np.array([["3*x-cos(y*z)"], 
              ["x**2-625*y**2"], 
              ["exp(-x*y)+20*z"]]) #(10*pi-3)/3=9.4719
    B = np.array([0.5, 0, -9.472])
    #Igualdad de la matriz
    
    print("\nMatriz A:\n")
    print(A)
    print("Igualdad Matriz A")
    print(B)
    
    A_jacobiana = operaciones.calcular_matriz_Jacobiana(A)
    print("\nMatriz Jacobiana\n")
    print(A_jacobiana)
    
    #En esta parte se cambian los valores iniciales de las variables 
    x_i = {x: 1, y: 2, z: 3} 
    row = 1
    error_tolerable = errores.calcular_error_tolerable(n)

    # Imprimir la cabecera de la tabla
    print(f"\n{'i':<3} | {'x1':<10} | {'x2':<10} | {'x3':<10} | {'Error relativo':<20}")
    print("-" * 50)
    
    while True:
        keys = [x, y, z]
        #Agregar la fila para agregarla a la matriz de valores
        new_row = np.array([row])
        new_row = np.hstack((new_row, list(x_i.values())))
        
        #Calcular valor nuevo de las variables
        array = operaciones.Newton_Raphson_Method(A, B, A_jacobiana, x_i, n)
        h_values = array[0]
        x_j = array[1]
        x_j = cifras_significativas.lista_cifras_significativas(x_j, n)
        
        #Meter los valores calculados a la fila nueva
        new_row = np.hstack((new_row, h_values))
        new_row = np.hstack((new_row, x_j))
        
        #Calcular los errores 
        errores_relativos = errores.calcular_errores_relativos(x_i.values(), x_j, n)
        
        # Imprimir los valores de la iteración actual
        print(f"{row:<3} | {x_j[0]:<10} | {x_j[1]:<10} | {x_j[2]:<10} | {errores_relativos[0]:<20}")
        
        #Meter errores relativos a la fila
        new_row = np.hstack((new_row, errores_relativos))
        if matriz.size == 0:
            matriz = new_row
        else:
            matriz = np.vstack((matriz, new_row))
            
        #Errores relativos
        if all(error < error_tolerable for error in errores_relativos):
            soluciones = x_j
            break
        if row > 500:
            print("La funcion no  convergio, inserte otros valores")
            break
        x_i = dict(zip(keys, x_j))
        row += 1
        
    return [matriz, soluciones]

def main():
    print("-------------------METODO NEWTON-RAPHSON-------------------")
    asks=Asks()
    
    while True:
        n = asks.ask_for_int("con cuantas cifras significativas desea trabajar?")
        if n < 1:
            print("El minimo de cifras significativas es 1, intentalo de nuevo")            
        else:                     
            break
    array = Newton_raphson(n)
    soluciones = array[1]
    if len(soluciones) != 0:
        print(f"\nSOLUCIONES:")
        for i in range(len(soluciones)):
            print(f"X_{i + 1}: {soluciones[i]}")

if __name__ == "__main__":
    main()