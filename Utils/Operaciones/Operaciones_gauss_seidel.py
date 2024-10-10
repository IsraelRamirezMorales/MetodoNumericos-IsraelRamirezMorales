import numpy as np
from Utils.Cifras_significativas import Cifras_significativas
class Operaciones_gauss_seidel:
    def Operacion_Gauss_Seidel(self,T, x_i, C, n):
        cifras_significativas=Cifras_significativas()
        x_gauss_seidel = np.empty(x_i.size)
        for k in range(x_i.size):
            value = (cifras_significativas.vector_cifras_significativas(np.dot(T, x_i), n) + cifras_significativas.vector_cifras_significativas(C, n))[k]
            x_gauss_seidel[k] = value
            x_i[k] = value   
        x_gauss_seidel = cifras_significativas.vector_cifras_significativas(x_gauss_seidel, n)
        return x_gauss_seidel
    
    def SOR(self,x_i, x_j, w, n):
        cifras_significativas=Cifras_significativas()
        x_sor = np.empty(x_i.size)
        i = 0
        for sor_anterior,seidel in zip(x_i, x_j):
            value = w*(seidel) + (1-w)*(sor_anterior)
            x_sor[i] = value
            i += 1
        x_sor = cifras_significativas.vector_cifras_significativas(x_sor, n)
        return x_sor
    