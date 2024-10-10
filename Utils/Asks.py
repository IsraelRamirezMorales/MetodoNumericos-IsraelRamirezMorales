
class Asks:
    def ask_for_double(self, nombre_valor):  
        while True:
            try:
                return float(input(f"Ingresa {nombre_valor}: "))
            except Exception as e:
                print("Valor invalido, intentelo de nuevo")

    def ask_for_int(self, nombre_valor):  
        while True:
            try:
                return int(input(f"Ingresa {nombre_valor}: "))
            except Exception as e:
                print("Valor invalido, intentelo de nuevo")
