import numpy as np

def coeficientes_polinomio_interpolante(x_values, y_values):
    """
    Calcula los coeficientes de un polinomio interpolante que pasa por los puntos dados (x_values, y_values).
    
    Parámetros:
    x_values : lista de valores x conocidos
    y_values : lista de valores y conocidos (f(x) en los puntos x)
    
    Retorna:
    coeficientes : lista de coeficientes [a0, a1, ..., an] del polinomio interpolante
                   donde el polinomio es a0 + a1*x + a2*x^2 + ... + an*x^n
    """
    
    n = len(x_values)
    
    # Construcción de la matriz del sistema según la forma de la pizarra
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = x_values[i] ** j
    
    # Vector de resultados
    B = np.array(y_values)
    
    # Resolución del sistema lineal para encontrar los coeficientes
    coeficientes = np.linalg.solve(A, B)
    
    return coeficientes

# Ejemplo de uso
x_values = [1, 2, 5, 10]  # [1, 2, 3, 4, 5]Valores x conocidos
y_values = [1, 4, 25, 100]  #[1, 0.5, 0.3333, 0.25, 0.2] Valores y conocidos correspondientes

coeficientes = coeficientes_polinomio_interpolante(x_values, y_values)
print(f"Coeficientes del polinomio interpolante: {coeficientes}")

# Formato del polinomio
polinomio_str = ' + '.join([f"{coef:.4f}*x^{i}" for i, coef in enumerate(coeficientes)])
print(f"\nEl polinomio interpolante es aproximadamente: {polinomio_str}")

