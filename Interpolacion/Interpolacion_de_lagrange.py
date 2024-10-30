import numpy as np

def Interpolacion_de_lagrange(x_values, y_values, x):
    
    """
    Calcula el valor del polinomio de interpolación de Lagrange
    en un punto x dado, basado en los puntos (x_values, y_values).
    
    Parámetros:
    x_values : lista de puntos x conocidos
    y_values : lista de puntos y conocidos (f(x) en los puntos x)
    x        : valor en el cual se evaluará el polinomio
    
    Retorna:
    p_x : valor del polinomio en x
    """
    
    n = len(x_values)
    p_x = 0  # Polinomio evaluado en x

    for i in range(n):
        # Calcular el término de Lagrange para el i-ésimo punto
        term = y_values[i]
        print(f"\nCalculando el término para i = {i} (y[{i}] = {y_values[i]})")
        
        for j in range(n):
            if i != j:
                factor = (x - x_values[j]) / (x_values[i] - x_values[j])
                term *= factor
                print(f"  Multiplicando por (({x} - {x_values[j]}) / ({x_values[i]} - {x_values[j]})) = {factor:.4f}")
                print(f"  Término temporal: {term:.4f}")
        
        print(f"Término final para i = {i}: {term:.4f}")
        p_x += term
        print(f"Polinomio acumulado p_x: {p_x:.4f}")

    return p_x

x_values = [1, 2, 5, 10]  # Valores x conocidos
y_values = [1, 4, 25, 100]  # Valores y conocidos correspondientes a x
x = 7  # Punto donde queremos evaluar el polinomio

resultado = Interpolacion_de_lagrange(x_values, y_values, x)
print(f"\nEl valor del polinomio interpolante en x = {x} es aproximadamente {resultado}")
