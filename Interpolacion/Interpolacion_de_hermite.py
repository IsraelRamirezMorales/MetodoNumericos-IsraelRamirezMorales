import numpy as np
import math

def interpolacion_Hermite():
    x = np.array([1.3, 1.6, 1.9])    
    y = np.array([0.6201, 0.4554, 0.2818])
    y_ = np.array([-0.5220, -0.5699, -0.5812])
    print("f(x)= ESCRIBA VALOR")
    x_Valor = 11 
    print("Valor ingresado fue {}".format(x_Valor))
    
    x = crear_z(x)
    y = crear_z(y)
    y_ = crear_y_(y_)

    ejecutar(ecuacion(y, x, y_), cadena(x, x_Valor))

def crear_y_(y_):
    new_y_ = np.array([])
    j = 0
    for i in range(2 * len(y_)):
        if i % 2 == 0:
            new_y_ = np.append(new_y_, y_[j])
            j += 1
    return new_y_

def crear_z(y_):
    j = 0
    new_y_ = np.array([])
    new_y_ = np.append(new_y_, y_[j])

    for i in range(2 * (len(y_)) - 1):
        new_y_ = np.append(new_y_, y_[j])
        if i % 2 == 0:
            j += 1
        i += 1
    print(new_y_)
    return new_y_

def ecuacion(y, x, y_):
    contador = len(y) - 1
    condicion, j, i, k = 0, len(y_) - 1, 0, 1
    primer_fila = np.array([])

    while True:
        primer_fila = np.append(primer_fila, y[i]) if contador == len(y) - 1 else primer_fila
        if contador == len(y) - 1:
            i += 1

        if y[contador] == y[contador - 1] and j > -1:
            y[contador] = y_[j]
            j -= 1
        else:
            y[contador] = (y[contador] - y[contador - 1]) / (x[contador] - x[contador - 2])

        contador -= 1

        contador = contador if contador > condicion else len(y) - 1
        if len(primer_fila) == len(y):
            print("primer_fila")
            print(primer_fila)
            break

    return primer_fila

def cadena(x, x_valor):
    i = 0
    s = np.array([1])
    for j in range(len(x) - 1):
        s = np.append(s, s[i] * (x_valor - x[i]))
        i += 1
    print("s")
    print(s)
    return s

def ejecutar(s, f):
    print(s)
    print(f)
    resultado = s * f
    print(resultado)
    resultado = sum(resultado)
    print(resultado)
    return resultado

# Llamada a la función principal
interpolacion_Hermite()
