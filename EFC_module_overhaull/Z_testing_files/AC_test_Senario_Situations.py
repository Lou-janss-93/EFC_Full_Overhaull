# this test file is used to test the complete EFC module based on diffrent conditions
# and situations. It will test the complete EFC module and all its submodules.
# situations from everyday life will be used to test the EFC module.
# ranging from normal to extrme situations, good and bad normal situation to extreme good and bad situations.
# The test will be done by using the unittest module from python?
# Louis Janssens & GitHub Copilot - 19/05/2025

import unittest
from B_1core_module import CoreModule

class TestEFCSituations(unittest.TestCase):
    def setUp(self):
        self.core = CoreModule()

    def test_normal_good(self):
        # Normale positieve situatie
        self.core.process_text("I feel happy and relaxed at home.")
        # Geen assert: output visueel controleren of uitbreiden met logica

    def test_normal_bad(self):
        # Normale negatieve situatie
        self.core.process_text("I feel a bit tired and stressed after work.")

    def test_extreme_good(self):
        # Extreem positieve situatie
        self.core.process_text("I just won the lottery and everything is perfect!")

    def test_extreme_bad(self):
        # Extreem negatieve situatie
        self.core.process_text("I lost my job and my house burned down.")

    def test_neutral(self):
        # Neutrale situatie
        self.core.process_text("Today is just an average day.")

if __name__ == "__main__":
    unittest.main()