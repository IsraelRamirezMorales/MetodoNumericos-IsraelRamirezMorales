import numpy as np

def Extrapolacion_Richardson():
    x = np.array([0, 0.25, 0.5, 0.75, 1])
    y = np.array([1.2, 1.1035, 0.925, 0.6363, 0.2])
    val = (len(x) / 2) + 0.5
    h1 = x[len(x)-1] - x[0]
    h2 = x[len(x)-2] - x[1]
    D1 = (y[len(x)-1] - y[0]) / (x[len(x)-1] - x[0])
    D2 = (y[len(x)-2] - y[1]) / (x[len(x)-2] - x[1])
    print("D1: {}, D2: {}".format(D1, D2))
    
    if h2 == h1 / 2:
        Vv = ((4 * D2) - D1) / 3
        print("El resultado es  :{}".format(Vv))
    else:
        Vv = D2 + ((D2 - D1) / ((h1 / h2) ** 2 - 1))
        print("El resultado es :{}".format(Vv))

    return Vv

# Llamada a la función
Extrapolacion_Richardson()
