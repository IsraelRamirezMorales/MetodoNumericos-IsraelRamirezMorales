def primera_derivada(x, y, x_objetivo):
    # Encontrar los puntos más cercanos alrededor de x_objetivo
    i = x.index(x_objetivo)
    
    
    f_xm1 = y[i-1]
    f_xi = y[i]
    f_xp1 = y[i+1]
    
    # Calcular la primera derivada 
    derivada = (f_xm1 * ((2*x_objetivo - x[i] - x[i+1]) / ((x[i-1] - x[i]) * (x[i-1] - x[i+1])))) + \
                (f_xi * ((2*x_objetivo - x[i-1] - x[i+1]) / ((x[i] - x[i-1]) * (x[i] - x[i+1])))) + \
                (f_xp1 * ((2*x_objetivo - x[i-1] - x[i]) / ((x[i+1] - x[i]) * (x[i+1] - x[i-1]))))

    return derivada


def segunda_derivada(x, y, x_objetivo):
    # Encontrar los puntos más cercanos alrededor de x_objetivo
    i = x.index(x_objetivo)
    
    
    f_xm1 = y[i-1]
    f_xi = y[i]
    f_xp1 = y[i+1]
    
    # Calcular la segunda derivada 
    derivada_segunda = (f_xm1 * (2 / ((x[i-1] - x[i]) * (x[i-1] - x[i+1])))) + \
                        (f_xi * (2 / ((x[i] - x[i-1]) * (x[i] - x[i+1])))) + \
                        (f_xp1 * (2 / ((x[i+1] - x[i]) * (x[i+1] - x[i-1]))))

    return derivada_segunda


x=[0,1.25,3.75]
y=[13.5,12,10]


x_objetivo = float(input("Introduce el valor de x_objetivo: "))

try:
    
    derivada_primera = primera_derivada(x, y, x_objetivo)
    derivada_segunda = segunda_derivada(x, y, x_objetivo)
    
    
    print(f"\nPrimera derivada f'(x) en x = {x_objetivo}: {derivada_primera}")
    print(f"Segunda derivada f''(x) en x = {x_objetivo}: {derivada_segunda}")
    
except Exception as e:
    print(f"Error: {e}")








