# update.py

import sys
sys.path.append('/Users/57304/Documents/PARCIAL II PARTE 2')

from Modelos.Clientes import Cliente,clientes_registrados
from Modelos.Facturas import Factura





def actualizar_cliente(cedula, nombre):
    if cedula in clientes_registrados:
        clientes_registrados[cedula].nombre = nombre
        return True
    else:
        return False

def actualizar_factura(cliente, fecha, nuevos_productos):
    for factura in cliente.facturas:
        if factura.fecha == fecha:
            factura.productos_comprados = nuevos_productos
            return True
    return False

