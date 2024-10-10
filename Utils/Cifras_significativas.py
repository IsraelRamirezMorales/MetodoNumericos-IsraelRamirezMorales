import numpy as np
class Cifras_significativas:
    def valor_cifras_significativas(self,numero, n):
        if numero == 0:
            return 0
        else:
            numero_float = float(numero) 
            factor = n - (int(f"{numero_float:e}".split('e')[1]) + 1)
            return round(numero_float, factor)
    
    def vector_cifras_significativas(self,vector, n):
        new_vector = np.empty(vector.shape[0])
        for i in range(vector.shape[0]):
            new_vector[i] = self.valor_cifras_significativas(vector[i], n)
        return new_vector
    
    def vector_cifras_significativas_gauss(self,vector, n):
        new_vector = np.empty(vector.size)
        for i in range(vector.size):
            new_vector[i] = self.valor_cifras_significativas(vector[i], n)
        return new_vector
    
    def lista_cifras_significativas(self,lista, n):
        new_list = []
        for i in range(len(lista)):
            new_list.append(self.valor_cifras_significativas(lista[i], n))
        return new_list