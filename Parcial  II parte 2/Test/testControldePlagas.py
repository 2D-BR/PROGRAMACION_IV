import unittest

import sys
sys.path.append('/Users/57304/Documents/PARCIAL II PARTE 2')

from Modelos.ControldePlagas import ControlPlagas

class TestControlPlagas(unittest.TestCase):
    def setUp(self):
        # Crear instancias de ControlPlagas para las pruebas
        self.plaga1 = ControlPlagas(12345, "Plaga 1", "Quincenal", 50.0, 7)
        self.plaga2 = ControlPlagas(67890, "Plaga 2", "Mensual", 30.0, 14)

    def test_registro_ica(self):
        self.assertEqual(self.plaga1.registro_ica, 12345)
        self.assertEqual(self.plaga2.registro_ica, 67890)

    def test_nombre_producto(self):
        self.assertEqual(self.plaga1.nombre_producto, "Plaga 1")
        self.assertEqual(self.plaga2.nombre_producto, "Plaga 2")

    def test_frecuencia_aplicacion(self):
        self.assertEqual(self.plaga1.frecuencia_aplicacion, "Quincenal")
        self.assertEqual(self.plaga2.frecuencia_aplicacion, "Mensual")

    def test_valor_producto(self):
        self.assertEqual(self.plaga1.valor_producto, 50.0)
        self.assertEqual(self.plaga2.valor_producto, 30.0)

    def test_periodo_carencia(self):
        self.assertEqual(self.plaga1.periodo_carencia, 7)
        self.assertEqual(self.plaga2.periodo_carencia, 14)

if __name__ == '__main__':
    unittest.main()
