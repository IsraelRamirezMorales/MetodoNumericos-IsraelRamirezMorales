def regla_de_simpson_un_tercio(funcion_str, a, b, n):
    """
    Calcula la integral de una función en el intervalo [a, b] usando la regla de Simpson.

    Parámetros:
        funcion_str (str): La función a integrar en formato de cadena de texto (ej. 'math.exp(x**4)').
        a (float): Límite inferior de la integración.
        b (float): Límite superior de la integración.
        n (int): Número de subintervalos (debe ser par).

    Retorna:
        float: Aproximación de la integral de la función en [a, b].
    """
    # Comprobar si n es par
    if n % 2 != 0:
        raise ValueError("El número de subintervalos (n) debe ser par para la regla de Simpson.")
    
    # Calcular el ancho de cada subintervalo
    delta_x = (b - a) / n
    
    # Evaluar la función en los extremos del intervalo
    x = a
    integral = eval(funcion_str)  # f(a)
    x = b
    integral += eval(funcion_str)  # + f(b)
    
    # Sumar los valores de la función en los puntos intermedios
    for i in range(1, n):
        x = a + i * delta_x
        coeficiente = 4 if i % 2 != 0 else 2  # 4 para impares, 2 para pares
        integral += coeficiente * eval(funcion_str)
    
    # Multiplicar por el factor de la regla de Simpson
    integral *= delta_x / 3
    
    return integral

# Ejemplo de uso
import math

# Definir la función como una cadena de texto para e^x^4
funcion_str = "math.exp(x**4)"

# Parámetros de la integral
a = -1             # Límite inferior
b = 1              # Límite superior
n = 6              # Número de subintervalos (debe ser par)

# Calcular la integral
resultado = regla_de_simpson_un_tercio(funcion_str, a, b, n)
print(f"La integral aproximada de {funcion_str} en [{a}, {b}] es:", resultado)
