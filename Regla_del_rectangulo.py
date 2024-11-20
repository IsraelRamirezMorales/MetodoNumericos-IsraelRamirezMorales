def regla_del_rectangulo(funcion_str, a, b, n):
    """
    Calcula la integral de una función en el intervalo [a, b] usando la regla del rectángulo.

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
    
    # Inicializar la suma
    integral = 0.0
    
    # Sumar las áreas de cada rectángulo
    for i in range(n):
        x = a + i * delta_x  # Punto izquierdo del intervalo
        # Evaluar la función en x usando eval
        integral += eval(funcion_str) * delta_x
    
    return integral

# Ejemplo de uso
import math

# Definir la función como una cadena de texto para e^x^4
funcion_str = "math.exp(x**4)"

# Parámetros de la integral
a = -1             # Límite inferior
b = 1              # Límite superior
n = 5         # Número de subintervalos

# Calcular la integral
resultado = regla_del_rectangulo(funcion_str, a, b, n)
print(f"La integral aproximada de {funcion_str} en [{a}, {b}] es:", resultado)
