import unittest
from dof_reality.serial_comm import degrees_to_value, clamp_value
from dof_reality import config

class TestSerialComm(unittest.TestCase):

    def test_clamp_value(self):
        """ Vérifie que clamp_value limite bien les valeurs entre les bornes définies. """
        self.assertEqual(clamp_value(50, -100, 100), 50)
        self.assertEqual(clamp_value(150, -100, 100), 100)
        self.assertEqual(clamp_value(-150, -100, 100), -100)

    def test_degrees_to_value(self):
        """ Vérifie la conversion des degrés en valeurs 0-1024 en respectant les limites. """
        max_degrees = config.MAX_DEGREES

        # Test conversion sans dépassement
        self.assertEqual(degrees_to_value(0), 512)  # Neutre
        self.assertEqual(degrees_to_value(max_degrees), 1024)  # Max positif
        self.assertEqual(degrees_to_value(-max_degrees), 0)  # Max négatif

        # Test conversion avec dépassement et facteur multiplicateur
        config.MULTIPLIER_FACTOR = 1.5  # Simuler un gain
        self.assertEqual(degrees_to_value(max_degrees * 1.5), 1024)  # Clampé à 1024
        self.assertEqual(degrees_to_value(-max_degrees * 1.5), 0)  # Clampé à 0


if __name__ == '__main__':
    unittest.main()