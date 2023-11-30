
clientes_registrados = {}

# Clase Cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.facturas = []