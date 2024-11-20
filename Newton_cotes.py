import numpy as np

def newton_cotes():
    x = np.array([0.2, 0.4, 0.6, 0.8])
    fx = np.array([1.288, 2.456, 3.464, 4.528])
    a, b, R, i, posiciones = 0, 0.8, 0, -1, 0
    
    # Eliminar el elemento en el índice 2 (el número 3 en este caso)
    existe_b = b in x
    existe_a = a in x
    if existe_b:
        posiciones = np.where(x == b)
    if existe_a:
        posiciones = np.where(x == a)
    
    fx = np.delete(fx, posiciones)

    h = b - a
    if len(x) - 1 == 1:
        R = (h / 1) * fx[i + 1]
    if len(x) - 1 == 2:
        R = (h / 2) * (fx[i + 1] + fx[i + 2])
    if len(x) - 1 == 3:
        R = (h / 3) * (2 * fx[i + 1] + fx[i + 2] + 2 * fx[i + 3])
    if len(x) - 1 == 4:
        R = (h / 4) * (11 * fx[i + 1] + fx[i + 2] + fx[i + 3] + 11 * fx[i + 4])
    if len(x) - 1 == 5:
        R = (h / 5) * (11 * fx[i + 1] + 14 * fx[i + 2] + 26 * fx[i + 3] + 14 * fx[i + 4] + 11 * fx[i + 5])

    print("El resultado de la integral es: ",R)
    return

# Llamada a la función
newton_cotes()
