def regla_del_trapecio(funcion_str, a, b, n):
    """
    Calcula la integral de una función en el intervalo [a, b] usando la regla del trapecio.

    Parámetros:
        funcion_str (str): La función a integrar en formato de cadena de texto (ej. 'math.exp(x**4)').
        a (float): Límite inferior de la integración.
        b (float): Límite superior de la integración.
        n (int): Número de subintervalos.

    Retorna:
        float: Aproximación de la integral de la función en [a, b].
    """
    # Calcular el ancho de cada subintervalo
    delta_x = (b - a) / n
    
    # Evaluar la función en los extremos del intervalo
    x = a
    integral = eval(funcion_str) / 2  # f(a) / 2
    x = b
    integral += eval(funcion_str) / 2  # + f(b) / 2
    
    # Sumar las áreas de los trapecios en los puntos intermedios
    for i in range(1, n):
        x = a + i * delta_x  # Punto intermedio
        integral += eval(funcion_str)  # f(x_i)
    
    # Multiplicar por el ancho del trapecio
    integral *= delta_x
    
    return integral

# Ejemplo de uso
import math

# Definir la función como una cadena de texto para e^x^4
funcion_str = "math.exp(x**4)"

# Parámetros de la integral
a = -1             # Límite inferior
b = 1              # Límite superior
n = 5              # Número de subintervalos

# Calcular la integral
resultado = regla_del_trapecio(funcion_str, a, b, n)
print(f"La integral aproximada de {funcion_str} en [{a}, {b}] es:", resultado)