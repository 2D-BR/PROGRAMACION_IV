# read.py

import sys
sys.path.append('/Users/57304/Documents/PARCIAL II PARTE 2')

from Modelos.Clientes import Cliente,clientes_registrados
from Modelos.Facturas import Factura


def leer_cliente(cedula):
    if cedula in clientes_registrados:
        return clientes_registrados[cedula]
    else:
        return None

def leer_factura(cliente, fecha):
    for factura in cliente.facturas:
        if factura.fecha == fecha:
            return factura
    return None

