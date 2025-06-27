"""Tests unitaires pour SimpleMath."""

import unittest
from code import SimpleMath


class TestSimpleMath(unittest.TestCase):
    """Classe de tests pour les méthodes de SimpleMath."""

    def test_addition(self):
        """Teste la méthode addition."""
        self.assertEqual(SimpleMath.addition(2, 3), 5)

    def test_soustraction(self):
        """Teste la méthode soustraction."""
        self.assertEqual(SimpleMath.soustraction(5, 2), 3)


if __name__ == '__main__':
    unittest.main()
