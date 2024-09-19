import math

def f(x):
    """
    Definir la función original f(x) cuya raíz se quiere encontrar.
    Cambia esta función según la ecuación que quieras resolver.
    """
    return math.exp(x) - (4*x) 

def g(x):
    """
    Definir la función g(x) para el método de Punto Fijo.
    Esta función se usa para encontrar el valor iterativo de x.
    Cambia esta función según la ecuación que quieras resolver.
    """
    return 0.25*(math.exp(x))  

def calcular_error_tolerable(n):
    """
    Calcula el error tolerable en función del número de cifras significativas.
    
    :param n: Número de cifras significativas
    :return: Error tolerable
    """
    return 0.5 * (10 ** (2 - n))

def calcular_error_relativo(valor_anterior, valor_actual):
    """
    Calcula el error relativo entre un valor anterior y un valor actual.
    
    :param valor_anterior: Valor de la iteración anterior
    :param valor_actual: Valor de la iteración actual
    :return: Error relativo
    """
    return abs((valor_anterior - valor_actual) / valor_actual) * 100

def redondear_a_cifras_significativas(valor, cifras):
    """
    Redondea un número al número especificado de cifras significativas.
    
    :param valor: Número a redondear
    :param cifras: Número de cifras significativas
    :return: Número redondeado
    """
    if valor == 0:
        return 0
    else:
        return round(valor, cifras - int(math.floor(math.log10(abs(valor)))) - 1)

def punto_fijo(x0, tol, max_iter, cifras):
    """
    Método de Punto Fijo para resolver la ecuación x = g(x).
    
    x0: Valor inicial de la iteración
    tol: Tolerancia para detener las iteraciones
    max_iter: Número máximo de iteraciones permitidas
    cifras: Número de cifras significativas
    return: Aproximación de la raíz
    """
    print(f"{'i':<5}{'xi':<15}{'f(x_i)':<15}{'xi+1':<15}{'Error Relativo':<15}")
    print("-" * 65)

    xi = x0  # Valor inicial
    for i in range(0, max_iter + 1):
        # Calcular el nuevo valor xi+1 usando g(xi)
        xi_nuevo = g(xi)

        # Evaluar la función f(xi)
        f_xi = f(xi)

        # Redondear los valores a las cifras significativas deseadas
        xi_red = redondear_a_cifras_significativas(xi, cifras)
        xi_nuevo_red = redondear_a_cifras_significativas(xi_nuevo, cifras)
        f_xi_red = redondear_a_cifras_significativas(f_xi, cifras)

        # Calcular el error relativo
        if xi_nuevo != 0:
            Er = calcular_error_relativo(xi, xi_nuevo)
        else:
            Er = float('inf')

        Er_red = redondear_a_cifras_significativas(Er, cifras)

        # Imprimir los resultados de la iteración
        print(f"{i:<5}{xi_red:<15}{f_xi_red:<15}{xi_nuevo_red:<15}{Er_red:<15}")

        # Verificar si el error relativo es menor que la tolerancia
        if Er < tol:
            return xi_nuevo_red

        # Actualizar el valor de xi
        xi = xi_nuevo

    # Si no se encontró la raíz dentro del número máximo de iteraciones
    raise ValueError("El método no convergió en el número máximo de iteraciones.")

def main():
    """
    Función principal para solicitar datos al usuario y ejecutar el método de Punto Fijo.
    """
    print("Bienvenido al método de Punto Fijo")

    # Solicitar el número de cifras significativas
    while True:
        try:
            n = int(input("Ingrese el número de cifras significativas con el que desea trabajar (n): "))
            if n < 1:
                print("El número de cifras significativas debe ser mayor a 0, intente de nuevo.")
            else:
                break
        except ValueError:
            print("Entrada inválida, intente de nuevo.")

    # Calcular el error tolerable
    tol = calcular_error_tolerable(n)

    # Solicitar el valor inicial de x0
    while True:
        try:
            x0 = float(input("Ingrese el valor inicial x0: "))
            break
        except ValueError:
            print("Entrada inválida, intente de nuevo.")

    # Ejecutar el método de Punto Fijo
    try:
        resultado = punto_fijo(x0, tol, 100, n)  # 100 iteraciones como máximo
        print(f"\nLa raíz encontrada es: {resultado}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
