import unittest
from Modelos.ControldeFertilizantes import ControlFertilizantes

class TestControlFertilizantes(unittest.TestCase):
    def setUp(self):
       
        self.fertilizante1 = ControlFertilizantes(54321, "Fertilizante 1", "Mensual", 40.0, "2023-09-30")
        self.fertilizante2 = ControlFertilizantes(98765, "Fertilizante 2", "Semanal", 35.0, "2023-09-15")

    def test_registro_ica(self):
        self.assertEqual(self.fertilizante1.registro_ica, 54321)
        self.assertEqual(self.fertilizante2.registro_ica, 98765)

    def test_nombre_producto(self):
        self.assertEqual(self.fertilizante1.nombre_producto, "Fertilizante 1")
        self.assertEqual(self.fertilizante2.nombre_producto, "Fertilizante 2")

    def test_frecuencia_aplicacion(self):
        self.assertEqual(self.fertilizante1.frecuencia_aplicacion, "Mensual")
        self.assertEqual(self.fertilizante2.frecuencia_aplicacion, "Semanal")

    def test_valor_producto(self):
        self.assertEqual(self.fertilizante1.valor_producto, 40.0)
        self.assertEqual(self.fertilizante2.valor_producto, 35.0)

    def test_fecha_ultima_aplicacion(self):
        self.assertEqual(self.fertilizante1.fecha_ultima_aplicacion, "2023-09-30")
        self.assertEqual(self.fertilizante2.fecha_ultima_aplicacion, "2023-09-15")

if __name__ == '__main__':
    unittest.main()
