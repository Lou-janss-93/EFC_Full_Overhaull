# Louis Janssens & GitHub Copilot - 19/05/2025

from C_context_balans_module import ContextBalansModule
from D_context_situation_controle import ContextSituationControlModule
from E_primaire_secondarie_basicneeds import PrimaireSecondaireBasicNeedsModule
from F_calculate_module import calculate_core
from G_failsafe_module import EmergencyModule

def test_different_oss():
    """
    Test verschillende scenario's voor de EFC-modules.
    """
    w2c = 0.3
    w4p = 0.4
    w3c = 0.3
    gamma = 0.5
    delta = 0.5

    scenarios = [
        {"o2c": 50, "o4p": 70, "o3c": 60, "context": "Good", "primary_needs": [0.8, 0.9, 0.7], "secondary_needs": [0.6, 0.5, 0.4], "stimulus_intensity": 10, "evaluation": 0.8},
        {"o2c": 30, "o4p": 50, "o3c": 40, "context": "Bad", "primary_needs": [0.5, 0.6, 0.4], "secondary_needs": [0.3, 0.2, 0.1], "stimulus_intensity": 5, "evaluation": 0.5},
        {"o2c": 70, "o4p": 90, "o3c": 80, "context": "Light", "primary_needs": [0.9, 1.0, 0.8], "secondary_needs": [0.7, 0.6, 0.5], "stimulus_intensity": 15, "evaluation": 1.0},
        {"o2c": 20, "o4p": 40, "o3c": 30, "context": "Dark", "primary_needs": [0.4, 0.5, 0.3], "secondary_needs": [0.2, 0.1, 0.0], "stimulus_intensity": 3, "evaluation": 0.3},
        # Edge case: extreme balans
        {"o2c": 100, "o4p": 100, "o3c": 100, "context": "Bad", "primary_needs": [1.0, 1.0, 1.0], "secondary_needs": [1.0, 1.0, 1.0], "stimulus_intensity": 50, "evaluation": 2.0},
    ]

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n--- Scenario {i} ---")
        core_value = calculate_core(w2c, w4p, w3c, scenario["o2c"], scenario["o4p"], scenario["o3c"])
        context_balans = ContextBalansModule()
        context_balans.adjust_balance(scenario["context"])
        balans = context_balans.get_balance()
        basic_needs = PrimaireSecondaireBasicNeedsModule(0.6, 0.4, 0.3)
        P = basic_needs.bereken_P(scenario["primary_needs"], scenario["secondary_needs"], [1.0])
        context_situation = ContextSituationControlModule("TestSituation")
        S = scenario["stimulus_intensity"] * scenario["evaluation"]  # Simpel voorbeeld

        state = gamma * core_value + delta * (balans + P + S)
        print(f"Inputs: {scenario}")
        print(f"Core Value: {core_value}, Balans: {balans}, P: {P}, S: {S}, Overall State: {state}")

        # Assert dat de kernwaarde binnen een verwacht bereik valt
        assert -200 < core_value < 200, "Core value out of expected range"
        # Test response
        response = context_balans.respond(scenario["context"])
        print(f"Balans response: {response}")

        # Test failsafe
        failsafe = EmergencyModule("FailsafeTest")
        if state > 150 or state < -150:
            failsafe.block_system()
            assert failsafe.is_blocked(), "Failsafe should be triggered"
            print(failsafe.respond("test"))
        else:
            assert not failsafe.is_blocked(), "Failsafe should not be triggered"

if __name__ == "__main__":
    test_different_oss()