def diferencia_progresiva(x, y, x_objetivo):
    # Verifica que x_objetivo no sea el último punto
    if x_objetivo == x[-1]:
        raise ValueError("No se puede calcular la diferencia progresiva en el último punto.")
    
    # Encuentra el índice correspondiente al x_objetivo
    i = x.index(x_objetivo)
    
    derivada = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    return derivada

def diferencia_regresiva(x, y, x_objetivo):
    # Verifica que x_objetivo no sea el primer punto
    if x_objetivo == x[0]:
        raise ValueError("No se puede calcular la diferencia regresiva en el primer punto.")
    
    # Encuentra el índice correspondiente al x_objetivo
    i = x.index(x_objetivo)
    
    derivada = (y[i] - y[i - 1]) / (x[i] - x[i - 1])
    return derivada

def diferencia_central(x, y, x_objetivo):
    # Si x_objetivo está en la lista x, se usa su índice
    if x_objetivo in x:
        i = x.index(x_objetivo)
        # Verifica que x_objetivo no sea el primer ni el último punto
        if i == 0 or i == len(x) - 1:
            raise ValueError("No se puede calcular la diferencia central en los extremos de la tabla.")
    else:
        # Si x_objetivo no está en x, busca los puntos adyacentes
        menores = [xi for xi in x if xi < x_objetivo]
        mayores = [xi for xi in x if xi > x_objetivo]
        
        if not menores or not mayores:
            raise ValueError("No hay puntos adyacentes suficientes para calcular la diferencia central.")
        
        # Toma el mayor valor menor a x_objetivo y el menor valor mayor a x_objetivo
        x_menor = max(menores)
        x_mayor = min(mayores)
        
        # Encuentra los índices correspondientes
        i_menor = x.index(x_menor)
        i_mayor = x.index(x_mayor)
        
        
        derivada = (y[i_mayor] - y[i_menor]) / (x[i_mayor] - x[i_menor])
        return derivada
    
    
    derivada = (y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1])
    return derivada


x = [0, 2, 4, 6, 8, 10, 12]
y = [4, 5.5, 8, 13.5, 22, 31.5, 38]


x_objetivo_progresiva = float(input("Ingrese el valor de x para calcular la diferencia progresiva: "))
x_objetivo_central = float(input("Ingrese el valor de x para calcular la diferencia central: "))
x_objetivo_regresiva = float(input("Ingrese el valor de x para calcular la diferencia regresiva: "))


try:
    derivada_progresiva = diferencia_progresiva(x, y, x_objetivo_progresiva)
    print(f"Diferencia progresiva en x = {x_objetivo_progresiva}: {derivada_progresiva}")
except ValueError as e:
    print(e)

try:
    derivada_central = diferencia_central(x, y, x_objetivo_central)
    print(f"Diferencia central en x = {x_objetivo_central}: {derivada_central}")
except ValueError as e:
    print(e)

try:
    derivada_regresiva = diferencia_regresiva(x, y, x_objetivo_regresiva)
    print(f"Diferencia regresiva en x = {x_objetivo_regresiva}: {derivada_regresiva}")
except ValueError as e:
    print(e)
