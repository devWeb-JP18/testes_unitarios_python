import unittest
from app.matematica import Matematica

class testeMatematica(unittest.TestCase):

    def setUp(self):
        self.math = Matematica()
        

    def test_somar(self):
        self.assertEqual(5+3,8)

    def test_Soma(self):
        
        soma = self.math.somar(10,5)
        self.assertEqual(soma,15)

    def test_lista(self):
        self.assertIn(7,self.math.lista)

    """def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)"""

    def test_maior(self):
        self.assertGreaterEqual(5, 4)

    

