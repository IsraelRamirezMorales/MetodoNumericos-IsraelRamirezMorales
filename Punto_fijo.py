import numpy as np
import sympy as sp
import math
from Utils.Errores import Errores
from Utils.Asks import Asks
from Utils.Cifras_significativas import Cifras_significativas
from Utils.Operaciones.Operaciones_punto_fijo import Operaciones_punto_fijo

def Punto_fijo(n):
    # Inicializo los errores, cifras significativas,operaciones
    errores = Errores()
    operaciones = Operaciones_punto_fijo()
    cifras_significativas = Cifras_significativas()
    
    x, y, z = sp.symbols('x y z')  
    soluciones = []
    matrix = np.empty((0, 0))
    
    # Función original
    F = np.array([["3*x-cos(y*z)-0.5"], 
                  ["x**2-625*y**2"], 
                  ["exp(-x*y)+20*z+9.4719"]])
    
    G = np.array([["(0.5+cos(y*z))/3"], 
                  ["sqrt((x**2)/(625))"], 
                  ["(-9.4719-exp(-x*y))/20"]])
    
    print("\nFuncion F:\n", F)
    print("\nFuncion G:\n", G)
    
    x_i = {x: 0, y: 0, z: 0}  # Cambiar el valor inicial de las variables
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
        x_j = operaciones.Operacion_punto_fijo(G, x_i, n)  # Lista
        x_j = cifras_significativas.lista_cifras_significativas(x_j, n)
        
        #Calcular valor nuevo de las funciones
        functions = operaciones.calcular_funciones(F, dict(zip(keys, x_j)), n)
        functions = cifras_significativas.lista_cifras_significativas(functions, n)
        
        
        #Meter los valores calculados a la fila nueva
        new_row = np.hstack((new_row, x_j))
        new_row = np.hstack((new_row, functions))
        
        # Calcular error absoluto
        error_absoluto = errores.calcular_error_absoluto(x_i.values(), x_j, n)
        new_row = np.hstack((new_row, error_absoluto))
        
        # Calcular los errores 
        errores_relativos = errores.calcular_errores_relativos(x_i.values(), x_j, n)
        
        # Agregar los errores relativos a la fila
        new_row = np.hstack((new_row, errores_relativos))
        if matrix.size == 0:
            matrix = new_row
        else:
            matrix = np.vstack((matrix, new_row))
        
        # Imprimir los valores de la iteración actual
        print(f"{row:<3} | {x_j[0]:<10} | {x_j[1]:<10} | {x_j[2]:<10} | {errores_relativos[0]:<20}")
        
        #Errores relativos
        if all(error < error_tolerable for error in errores_relativos):
            soluciones = x_j
            break
        if row > 500:
            print("La función no convergió, inserte otros valores")
            break
        
        x_i = dict(zip(keys, x_j))
        row += 1
    
    return [matrix, soluciones]

def main():
    print("-------------------METODO PUNTO FIJO-------------------")
    asks = Asks()
    
    while True:
        n = asks.ask_for_int("¿Con cuántas cifras significativas desea trabajar?")
        if n < 1:
            print("El mínimo de cifras significativas es 1, inténtelo de nuevo")            
        else:
            break
    
    array = Punto_fijo(n)
    soluciones = array[1]
    
    if len(soluciones) != 0:
        print(f"\nSOLUCIONES:")
        for i in range(len(soluciones)):
            print(f"X_{i + 1}: {soluciones[i]}")

if __name__ == "__main__":
    main()
