def integracion_segmentos_desiguales(funcion_str, puntos):
    """
    Calcula la integral de una función en un conjunto de segmentos desiguales usando la regla del trapecio.

    Parámetros:
        funcion_str (str): La función a integrar en formato de cadena de texto (ej. 'math.exp(x**4)').
        puntos (list of float): Lista de puntos en el eje x donde se evalúa la función.

    Retorna:
        float: Aproximación de la integral de la función en los segmentos definidos por `puntos`.
    """
    import math
    
    # Inicializar la suma de la integral
    integral = 0.0
    
    # Calcular la integral en cada subintervalo [x_i, x_{i+1}]
    for i in range(len(puntos) - 1):
        # Punto izquierdo y derecho del subintervalo
        x_i = puntos[i]
        x_ip1 = puntos[i + 1]
        
        # Evaluar la función en x_i y x_{i+1}
        x = x_i
        f_x_i = eval(funcion_str)
        x = x_ip1
        f_x_ip1 = eval(funcion_str)
        
        # Aplicar la regla del trapecio en este subintervalo
        integral += (f_x_i + f_x_ip1) / 2 * (x_ip1 - x_i)
    
    return integral

# Ejemplo de uso
import math

# Definir la función como una cadena de texto para e^(x^4)
funcion_str = "math.exp(x**4)"

# Lista de puntos desiguales en el eje x
puntos = [-1, -0.9,-0.7, -0.3, 0, 0.4, 1]

# Calcular la integral
resultado = integracion_segmentos_desiguales(funcion_str, puntos)
print(f"La integral aproximada de {funcion_str} en el intervalo definido por {puntos} es:", resultado)
