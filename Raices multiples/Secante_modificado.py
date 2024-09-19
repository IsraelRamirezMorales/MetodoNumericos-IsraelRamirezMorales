import math

def f(x):
    # Definir la función f(x)
    return x**3 - 5 * x**2 + 7 * x - 3

def f_prima(x):
    # Definir la derivada f'(x)
    return 3 * x**2 - 10 * x + 7

def u(x):
    # Calcular el valor de u(x) = f(x) / f'(x)
    return f(x) / f_prima(x)

def calcular_error_tolerable(n):
    # Calcular el error tolerable en función de las cifras significativas
    return 0.5 * (10 ** (2 - n))

def calcular_error_relativo(valor_anterior, valor_actual):
    # Calcular el error relativo entre el valor anterior y el actual
    return abs((valor_anterior - valor_actual) / valor_actual) * 100

def redondear_a_cifras_significativas(valor, cifras):
    # Redondear un número a las cifras significativas deseadas
    if valor == 0:
        return 0
    else:
        return round(valor, cifras - int(math.floor(math.log10(abs(valor)))) - 1)

def secante_modificado(xi, xi_1, tol, max_iter, cifras):
    """
    Método de Secante Modificado para encontrar la raíz.
    """
    print(f"{'i':<5}{'xi':<15}{'xi+1':<15}{'f(xi)':<15}{'f(xi+1)':<15}{'f\'(xi)':<15}{'f\'(xi+1)':<15}{'U(xi)':<15}{'U(xi+1)':<15}{'xi+2':<15}{'Error Relativo':<15}")
    print("-" * 155)

    for i in range(max_iter):
        # Evaluar la función f(xi) y f'(xi)
        f_xi = f(xi)
        f_xi_1 = f(xi_1)
        f_prima_xi = f_prima(xi)
        f_prima_xi_1 = f_prima(xi_1)
        u_xi = u(xi)
        u_xi_1 = u(xi_1)
        
        if u_xi - u_xi_1 == 0:
            print("Hay una división entre cero.")
            return None
        
        # Calcular el siguiente valor xi+2
        xi_2 = xi_1 - u_xi_1 * ((xi - xi_1) / (u_xi - u_xi_1))

        # Redondear los valores a las cifras significativas deseadas
        xi_red = redondear_a_cifras_significativas(xi, cifras)
        xi_1_red = redondear_a_cifras_significativas(xi_1, cifras)
        f_xi_red = redondear_a_cifras_significativas(f_xi, cifras)
        f_xi_1_red = redondear_a_cifras_significativas(f_xi_1, cifras)
        f_prima_xi_red = redondear_a_cifras_significativas(f_prima_xi, cifras)
        f_prima_xi_1_red = redondear_a_cifras_significativas(f_prima_xi_1, cifras)
        xi_2_red = redondear_a_cifras_significativas(xi_2, cifras)
        u_xi_red = redondear_a_cifras_significativas(u_xi, cifras)
        u_xi_1_red = redondear_a_cifras_significativas(u_xi_1, cifras)

        # Calcular el error relativo
        Er = calcular_error_relativo(xi_1, xi_2)
        Er_red = redondear_a_cifras_significativas(Er, cifras)

        # Imprimir los resultados de la iteración
        print(f"{i:<5}{xi_red:<15}{xi_1_red:<15}{f_xi_red:<15}{f_xi_1_red:<15}{f_prima_xi_red:<15}{f_prima_xi_1_red:<15}{u_xi_red:<15}{u_xi_1_red:<15}{xi_2_red:<15}{Er_red:<15}")

        # Verificar si el error relativo es menor que la tolerancia
        if Er < tol:
            return redondear_a_cifras_significativas(xi_2, cifras)

        # Actualizar los valores para la siguiente iteración
        xi, xi_1 = xi_1, xi_2

    raise ValueError("El método no convergió en el número máximo de iteraciones.")

def main():
    print("BIENVENIDO AL MÉTODO SECANTE MODIFICADO")

    # Solicitar el número de cifras significativas
    while True:
        try:
            n = int(input("Ingrese el número de cifras significativas con el que desea trabajar: "))
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
            xi_1 = float(input("Ingrese el valor de (xi+1): "))
            break
        except ValueError:
            print("Entrada inválida, intente de nuevo.")
    
    try:
        resultado = secante_modificado(xi, xi_1, tol, 100, n)  # 100 iteraciones como máximo
        print(f"\nLa raíz encontrada es: {resultado}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
