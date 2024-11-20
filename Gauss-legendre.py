import numpy as np

# Definimos la función a integrar
def f(x):
    return np.exp(-x**2)

# Implementación de Gauss-Legendre
def gauss_legendre(f, a, b, n):
    """
    Calcula la integral de f en el intervalo [a, b] usando la cuadratura de Gauss-Legendre.
    
    Parámetros:
        f: función a integrar.
        a: límite inferior del intervalo.
        b: límite superior del intervalo.
        n: número de puntos de Gauss-Legendre (puede ser 1, 2, 3, 4, 5, o 6).

    Retorna:
        integral: valor aproximado de la integral.
    """
    
    # Pesos y puntos según la tabla de Gauss-Legendre para diferentes n
    if n == 1:
        x = np.array([0.0])
        w = np.array([2.0])
    elif n == 2:
        x = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
        w = np.array([1.0, 1.0])
    elif n == 3:
        x = np.array([0.0, -np.sqrt(3/5), np.sqrt(3/5)])
        w = np.array([8/9, 5/9, 5/9])
    elif n == 4:
        x = np.array([-np.sqrt((3 + 2*np.sqrt(6/5))/5), np.sqrt((3 + 2*np.sqrt(6/5))/5)])
        w = np.array([18/36, 18/36])
    elif n == 5:
        x = np.array([-np.sqrt(5 + 2*np.sqrt(10/7))/5, np.sqrt(5 + 2*np.sqrt(10/7))/5])
        w = np.array([8/10, 8/10])
    elif n == 6:
        x = np.array([0, -np.sqrt(3/7 + 4/35), np.sqrt(3/7 + 4/35)])
        w = np.array([5/9, 8/9])
    else:
        raise ValueError("El número de puntos debe ser entre 1 y 6")

    # Calculo de la integral usando el cambio de variable para el intervalo [a, b]
    integral = 0.0
    for i in range(n):
        # Cambio de variable al intervalo [a, b]
        xi = 0.5 * (b - a) * x[i] + 0.5 * (b + a)  # mapeo de [-1, 1] a [a, b]
        integral += w[i] * f(xi)
    
    # Multiplicar por el factor de escala (b - a)/2
    integral *= 0.5 * (b - a)
    
    return integral

# Intervalo y número de puntos
a = 1
b = 1.5  # Puedes cambiar el intervalo si es necesario
n = 3  # Cambia el número de puntos según la tabla (puede ser 1, 2, 3, 4, 5 o 6)

# Calculamos la integral
resultado = gauss_legendre(f, a, b, n)
print(f"Resultado de la integral usando Gauss-Legendre con {n} puntos: {resultado}")
