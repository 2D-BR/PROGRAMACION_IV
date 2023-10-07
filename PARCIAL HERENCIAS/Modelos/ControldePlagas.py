#ControldePlagas.py

from Modelos.ProductosdeControl import ProductoControl

# Subclase para Control de Plagas
class ControlPlagas(ProductoControl):
    def __init__(self, registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto, periodo_carencia):
        super().__init__(registro_ica, nombre_producto, frecuencia_aplicacion, valor_producto)
        self.periodo_carencia = periodo_carencia