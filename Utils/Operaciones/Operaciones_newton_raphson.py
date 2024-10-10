import numpy as np
import sympy as sp
from Utils.Cifras_significativas import Cifras_significativas
class Operaciones_newton_raphson:
    def calcular_matriz_Jacobiana(self,A):#valores como collection
        x, y, z = sp.symbols('x y z')
        variables = [x, y, z]
        jacobiana = np.empty((A.shape[0], A.shape[0]), dtype= object)
        for i in range(A.shape[0]):
            # Convertir la ecuación a una expresión simbólica
            expr = sp.sympify(A[i, 0])
            # Calcular la derivada parcial respecto a cada variable
            for j in range(len(variables)):
                derivada = sp.diff(expr, variables[j])
                jacobiana[i, j] = derivada
        return jacobiana

    def evaluar_matriz_Jacobiana(self,jacobiana, valores, n):#valores como collection
        cifras_significativas=Cifras_significativas()
        matriz = np.empty((jacobiana.shape[0], jacobiana.shape[0]))
        #valores como una collection
        for i in range(jacobiana.shape[0]):
            for j in range(jacobiana.shape[1]):
                expresion = sp.sympify(jacobiana[i, j])
                matriz[i, j] = cifras_significativas.valor_cifras_significativas(expresion.subs(valores), n)
        return matriz

    def calcular_minus_f(self,A, B, valores, n):#valores como collection
        cifras_significativas=Cifras_significativas()
        minus_f = np.empty(B.shape[0])
        for i in range(B.shape[0]):
            expresion = sp.sympify(A[i])
            minus_f[i] = B[i] - expresion.subs(valores)[0]
            minus_f[i] = cifras_significativas.valor_cifras_significativas(minus_f[i], n)
        return minus_f

    def Newton_Raphson_Method(self,A, B, A_jacobiana, x_i, n):
        cifras_significativas=Cifras_significativas()
        #x_i es una collection{x: 1, y: 2, z: 3}
        h_values = []#Guarda los valores de h
        x_j = []#Aquí se devolverán los siguientes valores del método
        #[C]{h_i} = [D] - Para crear el sistema de ecuaciones
        C = self.evaluar_matriz_Jacobiana(A_jacobiana, x_i, n)#Ya funciona
        D = self.calcular_minus_f(A, B, x_i, n)
        
        #Resolver el sistema de ecuaciones lineales
        h_values = np.linalg.solve(C, D).tolist()
        h_values = cifras_significativas.lista_cifras_significativas(h_values, n)
        for x_actual, h in zip(x_i.values(), h_values):
            x_j.append(cifras_significativas.valor_cifras_significativas((x_actual + h), n))
        return [h_values, x_j]