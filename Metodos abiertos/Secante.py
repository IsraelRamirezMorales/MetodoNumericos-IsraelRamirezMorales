import math

def f(x):
    """
    Definir la función original f(x) cuya raíz se quiere encontrar.
    Cambia esta función según la ecuación que quieras resolver.
    """
    f_x=x**2-7
    return f_x
         
def calcular_error_tolerable(n):
    """
    Calcula el error tolerable en función del número de cifras significativas.
    
    n: Número de cifras significativas
    """
    error_tolerable=0.5 * (10 ** (2 - n))
    return error_tolerable

def calcular_error_relativo(valor_anterior, valor_actual):
    """
    Calcula el error relativo entre un valor anterior y un valor actual.
    
    valor_anterior: Valor de la iteración anterior
    valor_actual: Valor de la iteración actual
    return: Error relativo
    """
    error_relativo=abs((valor_anterior - valor_actual) / valor_actual) * 100
    return error_relativo

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
        numero_redondeado=round(valor, cifras - int(math.floor(math.log10(abs(valor)))) - 1)
        return numero_redondeado

def secante(xi,xi_1, tol, max_iter, cifras):
    """
    Método de Secante para encontrar la raiz
    
    x0: Valor inicial de la iteración
    tol: Tolerancia para detener las iteraciones
    max_iter: Número máximo de iteraciones permitidas
    cifras: Número de cifras significativas
    return: Aproximación de la raíz
    """
    print(f"{'i':<5}{'xi':<15}{'xi+1':<15}{'f(xi)':<15}{'f(xi+1)':<15}{"xi+2":<15}{'Error Relativo':<15}")
    print("-" * 95)

    for i in range(0, max_iter + 1):
        
        # Evaluar la función f(xi) y f'(xi)
        f_xi = f(xi)
        f_xi_1=f(xi_1)
        
        if f_xi_1 - f_xi == 0:
            print("Hay una division entre cero.")
            return None
        
        #Formula para sacar xi+2
        xi_2=xi_1 - f_xi_1 * (xi_1 - xi) / (f_xi_1 - f_xi)

        # Redondear los valores a las cifras significativas deseadas
        xi_red = redondear_a_cifras_significativas(xi, cifras)
        xi_1_red=redondear_a_cifras_significativas(xi_1, cifras)
        f_xi_red = redondear_a_cifras_significativas(f_xi, cifras)
        f_xi_1_red=redondear_a_cifras_significativas(f_xi_1, cifras)
        xi_2_red=redondear_a_cifras_significativas(xi_2,cifras)
        
        # Calcular el error relativo
        if xi_2 != 0:
            Er = calcular_error_relativo(xi_1, xi_2)
        else:
            Er = float('inf')

        Er_red = redondear_a_cifras_significativas(Er, cifras)

        # Imprimir los resultados de la iteración
        print(f"{i:<5}{xi_red:<15}{xi_1_red:<15}{f_xi_red:<15}{f_xi_1_red:<15}{xi_2_red:<15}{Er_red:<15}")

        # Verificar si el error relativo es menor que la tolerancia
        if Er < tol:
            return xi_2

        # Actualizar el valor de xi
        xi = xi_1
        xi_1=xi_2

    # Si no se encontró la raíz dentro del número máximo de iteraciones
    raise ValueError("El método no convergió en el número máximo de iteraciones.")

def main():
   
    print("BIENVENIDO AL METODO (ABIERTO) SECANTE")

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

    # Solicitar los valores iniciales
    while True:
        try:
            xi = float(input("Ingrese el valor inicial (xi): "))
            xi_1 = float(input("Ingrese el valor de xi+1: "))
            break
        except ValueError:
            print("Entrada inválida, intente de nuevo.")
    
    try:
        resultado = secante(xi,xi_1, tol, 100, n)  # 100 iteraciones como máximo
        print(f"\nLa raíz encontrada es: {resultado}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
