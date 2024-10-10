import numpy as np
import sympy as sp
import math
from Utils.Errores import Errores
from Utils.Asks import Asks
from Utils.Cifras_significativas import Cifras_significativas
from Utils.Operaciones.Operaciones_gauss_seidel import Operaciones_gauss_seidel

def generar_matriz(numero_columnas): 
    matriz = np.array([3])
    if numero_columnas != 1:
        columna_nueva = np.array([3])
        for i in range(numero_columnas - 1):
            matriz = np.hstack((matriz, columna_nueva))
    return matriz    

def Gauss_Seidel(n, w):
    #Inicializo los errores, cifras significativas
    errores=Errores()
    operaciones=Operaciones_gauss_seidel()
    cifras_significativas = Cifras_significativas()
    soluciones = []
    matriz = np.empty((0,0))
    
    A = np.array([[-3, 4, 6], 
              [-1, -2, 3], 
              [1, 0, 1]])
    B = np.array([30, 8,6])
    
    '''
    #Coeficientes de la matriz
    A = np.array([[3, -1, -1], 
              [-1, 3, 1], 
              [2, 1, 4]])
    B = np.array([1, 3, 7])#Igualdad de la matriz
    
     F = np.array([["3*x-cos(y*z)-0.5"], 
              ["x**2-625*y**2"], 
              ["exp(-x*y)+20*z+9.4719"]]) 
                #(10*pi-3)/3=9.4719
    
    G = np.array([["(0.5+cos(y*z))/3"],["sqrt((x**2)/(625))"],["(-9.4719-exp(-x*y))/20"]])
    #Igualdad de la matriz
    '''
    
    # Imprimir el sistema de ecuaciones 
    print("\nSistema de ecuaciones:")
    for i in range(len(B)):
        equation = " + ".join([f"{A[i, j]} * x_{j + 1}" for j in range(len(A[i]))])
        print(f"{equation} = {B[i]}")
        
    print("\nMatriz A:")
    print(A)
    print("Igualdad Matriz A")
    print(B)
    
    #Cambiar el valor inicial de las variables
    x_i = np.zeros(len(B))
    D = np.diag(np.diag(A))
    print("\nDiagonal")
    print(D)
    
    D_inv = np.linalg.inv(D)
    print("\nDiagonal inversa")
    print(D_inv)
    
    Tx = D - A
    print("\nTx")
    print(Tx)
    
    T = np.dot(D_inv, Tx)
    print("\nT")
    print(T)
    
    C = np.dot(D_inv, B)
    print("\nC")
    print(C)
    
     # Imprimir la cabecera de la tabla
    print(f"\n{'i':<3} | {'x1':<10} | {'x2':<10} | {'x3':<10} | {'Error relativo':<20}")
    print("-" * 50)
    
    #Agregar valores inciales a la matriz
    row = 1
    error_tolerable = errores.calcular_error_tolerable(n)

    while True:
        #Crear la fila para agregarla a la matriz de valores
        new_row = np.array([row])
        new_row = np.hstack((new_row, x_i))
        
        #Sacar nuevo valor de las variables
        
        x_j = operaciones.Operacion_Gauss_Seidel(T, np.copy(x_i), C, n)
        
        #Usamos SOR
        x_sor = operaciones.SOR(x_i, x_j, w, n)
        
        #Metemos los valores a la fila nueva
        new_row = np.hstack((new_row, x_j))
        new_row = np.hstack((new_row, x_sor))
        
        
        
        #Errores
        if w == 1:
            errores_relativos = errores.calcular_errores_relativos(x_i, x_j, n)
        else:
            errores_relativos = errores.calcular_errores_relativos(x_j, x_sor, n)
            
        #Agregar los errores relativos a la fila
        new_row = np.hstack((new_row, errores_relativos))
        
        if matriz.size == 0:
            matriz = new_row
        else:
            matriz = np.vstack((matriz, new_row))
        
         # Imprimir los valores de la iteración actual
        print(f"{row:<3} | {x_j[0]:<10} | {x_j[1]:<10} | {x_j[2]:<10} | {errores_relativos[0]:<20}")
        
        #Verificar errores relativos
        if all(error < error_tolerable for error in errores_relativos):
            soluciones = x_j
            break
        if row > 500:
            print("La funcion no  convergio, inserte otros valores")
            break
        x_i = x_sor
        row += 1
        
    return [matriz, soluciones]

def main():
    
    asks=Asks()
    print("-------------------METODO GAUSS-SEIDEL-------------------")
    while True:
        n = asks.ask_for_int("con cuantas cifras significativas quiere trabajar")
        if n < 1:
            print("El minimo de cifras significativas es 1, intentalo de nuevo")            
        else:                     
            break
    while True:
        w = asks.ask_for_double("el coeficiente que desea utilizar para SOR")
        if w < 0:
            print("W tiene que ser mayor a 0")
        elif w < 1:
            print("Se hara una subrelajacion")
            break
        elif w == 1:
            print("El valor de w es 1, no cambiaran los calculos")
            break
        elif w < 2:
            print("Se hara una sobrerelajacion")
            break
        else:                     
            print("W es mayor o igual a 2, el sistema de ecuaciones divergera rapido")

    array = Gauss_Seidel(n , w)
    soluciones = array[1]
    if len(soluciones) != 0: 
        print(f"\nSOLUCIONES")
        for i in range(len(soluciones)):
            print(f"X_{i + 1}: {soluciones[i]}")
    

 
if __name__ == "__main__":
    main()