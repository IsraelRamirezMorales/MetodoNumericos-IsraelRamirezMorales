def regla_de_simpson_tres_octavos(funcion_str, a, b, n):
    """
    Calcula la integral de una función en el intervalo [a, b] usando la regla de Simpson 3/8.

    Parámetros:
        funcion_str (str): La función a integrar en formato de cadena de texto (ej. 'math.exp(x**4)').
        a (float): Límite inferior de la integración.
        b (float): Límite superior de la integración.
        n (int): Número de subintervalos (debe ser múltiplo de 3).

    Retorna:
        float: Aproximación de la integral de la función en [a, b].
    """
    # Comprobar si n es múltiplo de 3
    if n % 3 != 0:
        raise ValueError("El número de subintervalos (n) debe ser múltiplo de 3 para la regla de Simpson 3/8.")
    
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
        # Aplicar coeficientes: 3 para puntos intermedios, 1 para múltiplos de 3
        coeficiente = 3 if i % 3 != 0 else 1
        integral += coeficiente * eval(funcion_str)
    
    # Multiplicar por el factor de la regla de Simpson 3/8
    integral *= 3 * delta_x / 8
    
    return integral

# Ejemplo de uso
import math

# Definir la función como una cadena de texto para e^x^4
funcion_str = "x**2+3*x-9"

# Parámetros de la integral
a = 0             # Límite inferior
b = 4             # Límite superior
n = 3             # Número de subintervalos (debe ser múltiplo de 3)

# Calcular la integral
resultado = regla_de_simpson_tres_octavos(funcion_str, a, b, n)
print(f"La integral aproximada de {funcion_str} en [{a}, {b}] es:", resultado)
