#DAVID BUITRAGO RODRIGUEZ Y STEVEN AGUDELO
#UNIVERSIDAD TECNOLOGICA DE PEREIRA
#INGENIERIA EN SISTEMAS Y COMPUTACION
#PROGRAMACION IV

#clase productos de control 
class ProductoControl:
    #Constructor por defecto registro ICA, numero del producto, Nombre y valor.
    def __init__(self,registro_ica, nombre_producto,frecuencia_aplicacion,valor_producto ):
        self.registro_ica = registro_ica
        self.nombre_producto = nombre_producto
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor_producto = valor_producto

