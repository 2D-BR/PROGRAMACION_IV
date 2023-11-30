from Modelos.ControldePlagas import ControlPlagas
from Modelos.ControldeFertilizantes import ControlFertilizantes
from Modelos.Antibioticos import Antibiotico

# Clase Factura
class Factura:
    def __init__(self, fecha, cliente):
        self.fecha = fecha
        self.cliente = cliente
        self.productos_comprados = []  
        self.valor_total = 0.0  

    def agregar_producto(self, producto):
        self.productos_comprados.append(producto)
        self.valor_total += producto.valor_producto

    

    def __str__(self):
        factura_str = f"Factura del cliente {self.cliente.nombre} con fecha {self.fecha}. Valor total: ${self.valor_total:.2f}\n"
        if self.productos_comprados:
            factura_str += "Productos comprados:\n"
            for producto in self.productos_comprados:
                if isinstance(producto, ControlPlagas):
                    producto_str = f"Control de Plagas - Código: {producto.registro_ica}, Nombre: {producto.nombre_producto}, Valor: ${producto.valor_producto:.2f}\n"
                elif isinstance(producto, ControlFertilizantes):
                    producto_str = f"Control de Fertilizantes - Código: {producto.registro_ica}, Nombre: {producto.nombre_producto}, Valor: ${producto.valor_producto:.2f}\n"
                elif isinstance(producto, Antibiotico):
                    producto_str = f"Antibiótico - Nombre: {producto.nombre}, Valor: ${producto.valor_producto:.2f}\n"
                factura_str += producto_str
        return factura_str
