import math

def f(x):
    """
    Definir la función original f(x) cuya raíz se quiere encontrar.
    Cambia esta función según la ecuación que quieras resolver.
    """
    f_x=x**3-5*(x**2)+7*(x)-3
    return f_x

def f_prima(x):
    
    f_prima=3*(x**2)-10*(x)+7
    return f_prima

def f_biprima(x):
    
    f_biprima=6*(x)-10
    return f_biprima

def Xi_1(x):
    
    denominador=(f_prima(x)**2) - (f(x) * f_biprima(x))
    
    if denominador!=0:
        Xi_1=x-(f(x)*f_prima(x))/denominador
        return Xi_1 
    else:
        print("NO se puede dividir entre cero")
         

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
    
    valor: Número a redondear
    cifras: Número de cifras significativas
    return: Número redondeado
    """
    if valor == 0:
        return 0
    else:
        return round(valor, cifras - int(math.floor(math.log10(abs(valor)))) - 1)

def newton_raphson_modificado(x0, tol, max_iter, cifras):
    """
    Método de Newton Raphson modificado para encontrar la raiz
    
    x0: Valor inicial de la iteración
    tol: Tolerancia para detener las iteraciones
    max_iter: Número máximo de iteraciones permitidas
    cifras: Número de cifras significativas
    :return: Aproximación de la raíz
    """
    print(f"{'i':<5}{'xi':<15}{'f(xi)':<15}{'f_prima(xi)':<15}{'f_biprima(xi)':<15}{"xi+1":<15}{'Error Relativo':<15}")
    print("-" * 95)

    xi = x0  # Valor inicial
    for i in range(0, max_iter + 1):
        # Calcular el nuevo valor xi+1 
        xi_nuevo = Xi_1(xi)

        # Evaluar la función f(xi) y f'(xi)
        f_xi = f(xi)
        f_prima_xi=f_prima(xi)
        f_biprima_xi=f_biprima(xi)

        # Redondear los valores a las cifras significativas deseadas
        xi_red = redondear_a_cifras_significativas(xi, cifras)
        xi_nuevo_red = redondear_a_cifras_significativas(xi_nuevo, cifras)
        f_xi_red = redondear_a_cifras_significativas(f_xi, cifras)
        f_prima_xi_red=redondear_a_cifras_significativas(f_prima_xi, cifras)
        f_biprima_xi_red=redondear_a_cifras_significativas(f_biprima_xi, cifras)

        # Calcular el error relativo
        if xi_nuevo != 0:
            Er = calcular_error_relativo(xi, xi_nuevo)
        else:
            Er = float('inf')

        Er_red = redondear_a_cifras_significativas(Er, cifras)

        # Imprimir los resultados de la iteración
        print(f"{i:<5}{xi_red:<15}{f_xi_red:<15}{f_prima_xi_red:<15}{f_biprima_xi_red:<15}{xi_nuevo_red:<15}{Er_red:<15}")

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
    print("Bienvenido al método de Newton-Raphson-Modificado")

    # Solicitar el número de cifras significativas
    while True:
        try:
            n = int(input("Ingrese el número de cifras significativas con el que desea trabajar : "))
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
            x0 = float(input("Ingrese el valor inicial: "))
            break
        except ValueError:
            print("Entrada inválida, intente de nuevo.")
    # Ejecutar el método de Punto Fijo
    try:
        resultado = newton_raphson_modificado(x0, tol, 100, n)  # 100 iteraciones como máximo
        print(f"\nLa raíz encontrada es: {resultado}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()