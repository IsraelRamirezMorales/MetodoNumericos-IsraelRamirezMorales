import math
import sympy as sp
from Utils.Cifras_significativas import Cifras_significativas


class Operaciones_punto_fijo:
    def Operacion_punto_fijo(self,G, x_i, n): 
        cifras_significativas=Cifras_significativas()
        x, y, z = sp.symbols('x, y, z')
        keys = [x, y, z]
        valores = list(x_i.values()) #[0, 1]
        nuevos_valores = []
        
        for i in range(len(x_i)):
            expresion = sp.sympify(G[i, 0])
            value = cifras_significativas.valor_cifras_significativas(expresion.subs(dict(zip(keys, valores))), n)#el argumento debe ser una collection
            nuevos_valores.append(value)
            valores[i] = value
        return nuevos_valores

    def calcular_funciones(self,F, x_j, n):
        cifras_significativas=Cifras_significativas()
        funciones = []
        for i in range(len(x_j)):
            expresion = sp.sympify(F[i, 0])
            value = cifras_significativas.valor_cifras_significativas(expresion.subs(x_j), n)
            funciones.append(value)
        return funciones