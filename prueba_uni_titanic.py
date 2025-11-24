import unittest
import titanic

class probarr_codigo_titanic(unittest.TestCase):
    def test_titanic(self):
        resultado = titanic.datos_tripulacion
        self.assertEqual(resultado,"jajjaja")