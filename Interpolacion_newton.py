def Interpolacion_newton(x, y, x_objetivo):
    # Ordenar los puntos alrededor del valor objetivo para encontrar los más cercanos
    puntos_cercanos = sorted(x, key=lambda xi: abs(xi - x_objetivo))
    
    # Seleccionamos los valores más cercanos alrededor de x_objetivo
    x0, x1, x2 = sorted([puntos_cercanos[0], puntos_cercanos[1], puntos_cercanos[2]])
    y0, y1, y2 = y[x.index(x0)], y[x.index(x1)], y[x.index(x2)]
    
    # Calculamos la equisdistancia h
    h = x1 - x0  # Debe ser constante entre x0, x1 y x2
    
    # Calculamos k usando la fórmula k = (x_objetivo - x0) / h
    k = (x_objetivo - x0) / h
    
    # Calculamos la primera derivada
    f_prima = (1 / h) * ((y1 - y0) + ((2 * k - 1) / 2) * (y2 - 2 * y1 + y0))
    
    # Calculamos la segunda derivada 
    f_segunda = (1 / h**2) * (y2 - 2 * y1 + y0)
    
    return f_prima, f_segunda, x0, x1, x2, y0, y1, y2 


x = [3, 5, 8, 10, 12, 20]
y = [1, 10, 25, 55, 105, 240]

# Valor deseado
x_objetivo = float(input("Ingresa el valor de x deseado: "))


try:
    derivada, segunda_derivada, x0, x1, x2, y0, y1, y2 = Interpolacion_newton(x, y, x_objetivo)
    
    
    print(f"Valores seleccionados de la tabla para calcular las derivadas en x = {x_objetivo}:")
    print(f"{'x0':<10}{'y0':<10}{'x1':<10}{'y1':<10}{'x2':<10}{'y2':<10}")
    print(f"{x0:<10}{y0:<10}{x1:<10}{y1:<10}{x2:<10}{y2:<10}")
    
    
    print(f"\nResultado de la primera derivada f'(x) en x = {x_objetivo}: {derivada}")
    print(f"Resultado de la segunda derivada f''(x) en x = {x_objetivo}: {segunda_derivada}")
    
except Exception as e:
    print(f"Error: {e}")
