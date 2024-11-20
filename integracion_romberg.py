import numpy as np

def integracion_romberg():
    I1 = np.array([0.1728, 0.988, 1.3648, 1.4808, 1.4956])  # Valores iniciales
    I2 = np.array([])  # Arreglo vacío para los valores de integración de la siguiente iteración
    i, k, fin = 0, 2, len(I1)  # Variables para controlar el índice, el nivel de iteración y el fin del ciclo
    Flag = True  # Bandera para el bucle while

    while Flag:
        print("Iteración {}:".format(k))
        for j in range(len(I1)-1):  # Iterar sobre I1 hasta el penúltimo índice
            # Cálculo de la nueva aproximación de integración usando Romberg
            I2 = np.append(I2, ((4**(k-1) * I1[j+1]) - I1[j]) / (4**(k-1) - 1))
            print("{}*{} - {} / {} = {}".format(4**(k-1), I1[j+1], I1[j], (4**(k-1)-1), 
                                               ((4**(k-1) * I1[j+1]) - I1[j]) / (4**(k-1) - 1)))

        I1 = I2  # Actualizar I1 con los nuevos valores calculados en I2
        I2 = np.array([])  # Limpiar I2 para la siguiente iteración
        
        k += 1  # Incrementar el nivel de iteración
        if k > fin:  # Si se alcanza el nivel máximo de iteración, salir del bucle
            Flag = False

    print("Resultado final:", I1[-1])  # Mostrar el último valor calculado

# Llamada a la función
integracion_romberg()
