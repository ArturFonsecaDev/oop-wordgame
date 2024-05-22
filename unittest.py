import unittest
from classes import Forca

class TestForcaDesenhar(unittest.TestCase):

    def setUp(self):
        self.forca = Forca()

    def test_desenhar_single_letter_word_correct(self):
        self.forca.palavra_secreta = 'a'
        self.forca.letras_corretas = {'a'}
        self.forca.desenhar('a')
        self.assertEqual(self.forca.desenhar(), 'a')

    def test_desenhar_single_letter_word_incorrect(self):
        self.forca.palavra_secreta = 'a'
        self.forca.letras_corretas = set()
        self.forca.desenhar('b')
        self.assertEqual(self.forca.desenhar(), '_')

    def test_desenhar_single_letter_word_mixed_case(self):
        self.forca.palavra_secreta = 'a'
        self.forca.letras_corretas = {'A'}
        self.forca.desenhar('a')
        self.assertEqual(self.forca.desenhar(), 'a')

    def test_desenhar_single_letter_word_repeated_letter(self):
        self.forca.palavra_secreta = 'a'
        self.forca.letras_corretas = {'a'}
        self.forca.desenhar('a')
        self.forca.desenhar('a')
        self.assertEqual(self.forca.desenhar(), 'a')

    def test_desenhar_single_letter_word_no_input(self):
        self.forca.palavra_secreta = 'a'
        self.forca.letras_corretas = set()
        self.assertEqual(self.forca.desenhar(), '_')

if __name__ == '__main__':
    unittest.main()