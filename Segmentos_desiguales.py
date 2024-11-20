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
funcion_str = "x**2+3*x-9"

# Lista de puntos corregida
puntos = [
    0.0, -9.0,
    0.0333333, -8.89889,
    0.0666667, -8.79556,
    0.1, -8.69,
    0.133333, -8.58222,
    0.166667, -8.47222,
    0.2, -8.36,
    0.233333, -8.24556,
    0.266667, -8.12889,
    0.3, -8.01,
    0.333333, -7.88889,
    0.366667, -7.76556,
    0.4, -7.64,
    0.433333, -7.51222,
    0.466667, -7.38222,
    0.5, -7.25,
    0.533333, -7.11556,
    0.566667, -6.97889,
    0.6, -6.84,
    0.633333, -6.69889,
    0.666667, -6.55556,
    0.7, -6.41,
    0.733333, -6.26222,
    0.766667, -6.11222,
    0.8, -5.96,
    0.833333, -5.80556,
    0.866667, -5.64889,
    0.9, -5.49,
    0.933333, -5.32889,
    0.966667, -5.16556,
    1.0, -5.0,
    1.03333, -4.83222,
    1.06667, -4.66222,
    1.1, -4.49,
    1.13333, -4.31556,
    1.16667, -4.13889,
    1.2, -3.96,
    1.23333, -3.77889,
    1.26667, -3.59556,
    1.3, -3.41,
    1.33333, -3.22222,
    1.36667, -3.03222,
    1.4, -2.84,
    1.43333, -2.64556,
    1.46667, -2.44889,
    1.5, -2.25,
    1.53333, -2.04889,
    1.56667, -1.84556,
    1.6, -1.64,
    1.63333, -1.43222,
    1.66667, -1.22222,
    1.7, -1.01,
    1.73333, -0.795556,
    1.76667, -0.578889,
    1.8, -0.36,
    1.83333, -0.138889,
    1.86667, 0.0844444,
    1.9, 0.31,
    1.93333, 0.537778,
    1.96667, 0.767778,
    2.0, 1.0,
    2.03333, 1.23444,
    2.06667, 1.47111,
    2.1, 1.71,
    2.13333, 1.95111,
    2.16667, 2.19444,
    2.2, 2.44,
    2.23333, 2.68778,
    2.26667, 2.93778,
    2.3, 3.19,
    2.33333, 3.44444,
    2.36667, 3.70111,
    2.4, 3.96,
    2.43333, 4.22111,
    2.46667, 4.48444,
    2.5, 4.75,
    2.53333, 5.01778,
    2.56667, 5.28778,
    2.6, 5.56,
    2.63333, 5.83444,
    2.66667, 6.11111,
    2.7, 6.39,
    2.73333, 6.67111,
    2.76667, 6.95444,
    2.8, 7.24,
    2.83333, 7.52778,
    2.86667, 7.81778,
    2.9, 8.11,
    2.93333, 8.40444,
    2.96667, 8.70111,
    3.0, 9.0,
    3.03333, 9.30111,
    3.06667, 9.60444,
    3.1, 9.91,
    3.13333, 10.2178,
    3.16667, 10.5278,
    3.2, 10.84,
    3.23333, 11.1544,
    3.26667, 11.4711,
    3.3, 11.79,
    3.33333, 12.1111,
    3.36667, 12.4344,
    3.4, 12.76,
    3.43333, 13.0878,
    3.46667, 13.4178,
    3.5, 13.75,
    3.53333, 14.0844,
    3.56667, 14.4211,
    3.6, 14.76,
    3.63333, 15.1011,
    3.66667, 15.4444,
    3.7, 15.79,
    3.73333, 16.1378,
    3.76667, 16.4878,
    3.8, 16.84,
    3.83333, 17.1944,
    3.86667, 17.5511,
    3.9, 17.91,
    3.93333, 18.2711,
    3.96667, 18.6344,
    4.0, 19.0
]


# Calcular la integral
resultado = integracion_segmentos_desiguales(funcion_str, puntos)
print(f"La integral aproximada de {funcion_str} en el intervalo definido por {puntos} es:", resultado)
