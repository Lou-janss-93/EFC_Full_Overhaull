# Louis Janssens & GitHub Copilot - 19/05/2025

import unittest
from C_context_balans_module import ContextBalansModule
from E_primaire_secondarie_basicneeds import PrimaireSecondaireBasicNeedsModule
from D_context_situation_controle import ContextSituationControlModule
from F_calculate_module import calculate_core
from G_failsafe_module import EmergencyModule

class TestEFCModules(unittest.TestCase):
    def test_context_balans_module(self):
        mod = ContextBalansModule()
        mod.adjust_balance("Good")
        self.assertLess(mod.get_balance(), 0)
        mod.adjust_balance("Bad")
        self.assertGreaterEqual(mod.get_balance(), 0)

    def test_basic_needs_module(self):
        mod = PrimaireSecondaireBasicNeedsModule(0.6, 0.4, 0.3)
        p = mod.bereken_P([1, 1, 1], [1, 1, 1], [1])
        self.assertAlmostEqual(p, 3.3)

    def test_context_situation_module(self):
        mod = ContextSituationControlModule("Test")
        self.assertEqual(mod.process("happy"), "positive")
        self.assertEqual(mod.process("sad"), "negative")
        self.assertEqual(mod.process("neutral"), "neutral")

    def test_calculate_core(self):
        result = calculate_core(0.3, 0.4, 0.3, 50, 70, 60)
        self.assertAlmostEqual(result, 61.0)

    def test_failsafe_tag_out(self):
        failsafe = EmergencyModule("TestFailsafe")
        user = "testuser"
        for i in range(3):
            failsafe.register_attempt(user, "test")
        self.assertTrue(failsafe.is_blocked())
        self.assertIn(user, failsafe.tagged_out_users)

if __name__ == "__main__":
    unittest.main()