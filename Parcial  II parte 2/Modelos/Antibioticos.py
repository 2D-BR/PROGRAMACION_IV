# Clase Antibiotico
class Antibiotico:
    def __init__(self, nombre, dosis, tipo_animal, valor_producto):
        self.nombre = nombre
        self.validar_dosis(dosis)  # Validar la dosis al crear una instancia de Antibiotico
        self.tipo_animal = self.validar_tipo_animal(tipo_animal)  # También aquí se valida el tipo de animal
        self.valor_producto = valor_producto
    
    def validar_dosis(self, dosis):
        dosis_num = float(dosis.rstrip('Kg').replace(',', ''))  # Convertir la dosis a un número
        if 400 <= dosis_num <= 600:
            self.dosis = dosis
        else:
            raise ValueError("Dosis no válida. Debe estar entre 400Kg y 600Kg.")

    def validar_tipo_animal(self, tipo_animal):
        tipos_permitidos = ["bovinos", "caprinos", "porcinos", "bovino", "caprino", "porcino"]
        tipo_animal = tipo_animal.lower()
        if tipo_animal in tipos_permitidos:
            return tipo_animal
        else:
            raise ValueError("Tipo de animal no válido. Debe ser 'Bovinos', 'Caprinos' o 'Porcinos'.")
