import sympy as sp
import numpy as np

    

# Ejemplo de uso
x_vals = [1,2,5,10]  # Múltiples puntos
y_vals = [1,4,25,100]  # Valores correspondientes
x_deseada = 11  # Punto donde queremos evaluar la interpolación


resultado=y_vals[0]+((y_vals[0]-y_vals[1])/(x_vals[0]-x_vals[1]))*(x_deseada-x_vals[0])

print(f"El valor de la funcion en x = {x_deseada} es: {resultado}")  # Sin redondear
