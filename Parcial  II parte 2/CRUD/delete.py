# delete.py

import sys
sys.path.append('/Users/57304/Documents/PARCIAL II PARTE 2')


from Modelos.Clientes import clientes_registrados

def eliminar_cliente(cedula):
    if cedula in clientes_registrados:
        del clientes_registrados[cedula]
        return True
    else:
        return False

def eliminar_factura(cliente, fecha):
    for factura in cliente.facturas:
        if factura.fecha == fecha:
            cliente.facturas.remove(factura)
            return True
    return False

