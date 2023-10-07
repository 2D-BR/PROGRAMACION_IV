#ControldeFertilizantes.py
from Modelos.ProductosdeControl import ProductoControl

# Subclase para Control de Fertilizantes
class ControlFertilizantes(ProductoControl):
    def __init__(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto, fecha_ultima_aplicacion):
        super().__init__(registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion