import math
from Utils.Cifras_significativas import Cifras_significativas
class Errores:
    def calcular_error_tolerable(self,n):
        return 0.5*(math.pow(10, 2-n))

    def calcular_error_relativo(self,valor_anterior, valor_actual):
        return (abs(1 - (valor_anterior / valor_actual)))*100

    def calcular_errores_relativos(self,x_i, x_j, n):
        cifras_significativas=Cifras_significativas()
        errores = []
        for anterior, actual in zip(x_i, x_j):
            if round(abs(anterior-actual),n)==1/(math.pow(10,n-1)):
                error=0
            else:    
                error = cifras_significativas.valor_cifras_significativas(self.calcular_error_relativo(anterior, actual), n)
            errores.append(error)
        return errores
    
    def calcular_error_absoluto(self,x_i, x_j, n):
        cifras_significativas=Cifras_significativas()
        suma = 0
        for anterior, actual in zip(x_i, x_j):
            suma += math.pow(actual - anterior, 2)
        return cifras_significativas.valor_cifras_significativas(math.sqrt(suma), n)