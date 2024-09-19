import math

def f(x):
    
    #Función sobre la que se va a trabajar.
    return (math.exp(2 * x) - 3)

def calcular_error_tolerable(n):
    #n: Número de cifras significativas
    
    error_tolerable=0.5 * (10 ** (2 - n))
    return error_tolerable

def calcular_error_relativo(valor_anterior, valor_actual):
    """
    Calcula el error relativo entre un valor anterior y un valor actual.
    
    valor_anterior: Valor de la iteración anterior
    valor_actual: Valor de la iteración actual
    
    """
    error_relativo=abs((valor_anterior - valor_actual) / valor_actual) * 100
    return error_relativo

def redondear_a_cifras_significativas(valor, cifras):
    
    #valor: Número a redondear
    #cifras: Número de cifras significativas
    
    if valor == 0:
        return 0
    else:
        numero_redondeado=round(valor, cifras - int(math.floor(math.log10(abs(valor)))) - 1)
        return numero_redondeado

def falsa_posicion(a, b, tol, max_iter, cifras):
    """
    Método de falsa posición para encontrar la raíz de la ecuación f(x) = 0.
    
    :a: Límite inferior del intervalo inicial
    :b: Límite superior del intervalo inicial
    :tol: Tolerancia para la convergencia
    :max_iter: Número máximo de iteraciones
    :cifras: Número de cifras significativas
    
    """
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        raise ValueError("La función no cambia de signo en el intervalo dado.")
    
    print(f"{'i':<5}{'a':<10}{'b':<10}{'f(a)':<15}{'f(b)':<15}{'c':<10}{'f(c)':<15}{'Er':<15}")
    print("-" * 95)

    c = a 
    error_relativo = float('inf')  
    error_tolerable = tol

    for i in range(max_iter):
        # Calcular el punto de la falsa posición
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f(c)

        # Redondear valores a cifras significativas
        a_red = redondear_a_cifras_significativas(a, cifras)
        b_red = redondear_a_cifras_significativas(b, cifras)
        fa_red = redondear_a_cifras_significativas(fa, cifras)
        fb_red = redondear_a_cifras_significativas(fb, cifras)
        c_red = redondear_a_cifras_significativas(c, cifras)
        fc_red = redondear_a_cifras_significativas(fc, cifras)

        # Calcular el error relativo
        if c != 0:
            Er = calcular_error_relativo(a_red, c_red)
        else:
            Er = float('inf')

        Er_red = redondear_a_cifras_significativas(Er, cifras)

        # Imprimir la tabla de resultados
        print(f"{i:<5}{a_red:<10}{b_red:<10}{fa_red:<15}{fb_red:<15}{c_red:<10}{fc_red:<15}{Er_red:<15}")

        # Verificar la convergencia
        if Er < error_tolerable:
            return redondear_a_cifras_significativas(c, cifras)

        # Actualizar el intervalo
        R = fa * fc
        if R > 0:
            a = c
            fa = fc
        elif R == 0:
            return redondear_a_cifras_significativas(c, cifras)
        else:
            b = c
            fb = fc

    # Si no se ha encontrado la raíz en el número máximo de iteraciones
    raise ValueError("El método no convergió en el número máximo de iteraciones.")

def main():
    
    print("-BIENVENIDO AL METODO (CERRADO) FALSA POSICION-")

    while True:
        try:
            n = int(input("Ingrese el número de cifras significativas con el que desea trabajar : "))
            if n < 1:
                print("El número de cifras significativas debe ser mayor a 0, intente de nuevo.")
            else:
                break
        except Exception as e:
            print("Entrada inválida, intente de nuevo.")

    # Calcular el error tolerable
    tol = calcular_error_tolerable(n)
    
    while True:
        try:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))
            break
        except ValueError:
            print("Entrada inválida, intente de nuevo.")

    # Verificar si f(a) y f(b) cambian de signo
    F_a = f(a)
    F_b = f(b)
    if F_a * F_b > 0:
        print("La función no cambia de signo en el intervalo dado. Proponga nuevos valores.")
        return

    
    try:
        resultado = falsa_posicion(a, b, tol, 100, n)  # 100 iteraciones como máximo
        print(f"\nLa raíz encontrada es: {resultado}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
