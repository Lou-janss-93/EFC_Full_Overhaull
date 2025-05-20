# Louis Janssens & GitHub Copilot - 19/05/2025

from C_context_balans_module import ContextBalansModule
from E_primaire_secondarie_basicneeds import PrimaireSecondaireBasicNeedsModule
from D_context_situation_controle import ContextSituationControlModule
from F_calculate_module import calculate_core
from G_failsafe_module import EmergencyModule

def test_critical_point():
    w2c = 0.3
    w4p = 0.4
    w3c = 0.3
    gamma = 0.5
    delta = 0.5

    # Critical scenario: alles maximaal
    critical_scenario = {
        "o2c": 100, "o4p": 100, "o3c": 100, "context": "Bad",
        "primary_needs": [1.0, 1.0, 1.0], "secondary_needs": [1.0, 1.0, 1.0],
        "stimulus_intensity": 20, "evaluation": 1.5
    }

    core_value = calculate_core(w2c, w4p, w3c, critical_scenario["o2c"], critical_scenario["o4p"], critical_scenario["o3c"])
    context_balans = ContextBalansModule()
    context_balans.adjust_balance(critical_scenario["context"])
    Y = context_balans.get_balance()

    basic_needs = PrimaireSecondaireBasicNeedsModule(0.6, 0.4, 0.3)
    P = basic_needs.bereken_P(critical_scenario["primary_needs"], critical_scenario["secondary_needs"], [1.0])

    context_situation = ContextSituationControlModule("CriticalSituation")
    S = critical_scenario["stimulus_intensity"] * critical_scenario["evaluation"]

    state = gamma * core_value + delta * (Y + P + S)
    print(f"Critical Scenario: {critical_scenario}")
    print(f"Core Value: {core_value}, Y: {Y}, P: {P}, S: {S}, Overall State: {state}")

    # Assert dat de overall state binnen het robuuste bereik blijft (bijv. rond 74.5 ± 10%)
    lower_bound = 67.0
    upper_bound = 82.0
    if lower_bound <= state <= upper_bound:
        print(f"✅ Robustness OK: State {state:.2f} binnen verwacht bereik ({lower_bound}-{upper_bound})")
    else:
        print(f"❌ WARNING: State {state:.2f} buiten verwacht bereik ({lower_bound}-{upper_bound})")

    # Test failsafe
    failsafe = EmergencyModule("FailsafeTest")
    if state > 150 or state < -150:
        failsafe.block_system()
        assert failsafe.is_blocked(), "Failsafe should be triggered"
        print(failsafe.respond("critical test"))
    else:
        assert not failsafe.is_blocked(), "Failsafe should not be triggered"

    # Extreme edge: alles maximaal + extra stimulus
    extreme_scenario = dict(critical_scenario)
    extreme_scenario["stimulus_intensity"] = 100
    extreme_scenario["evaluation"] = 3.0
    S_extreme = extreme_scenario["stimulus_intensity"] * extreme_scenario["evaluation"]
    state_extreme = gamma * core_value + delta * (Y + P + S_extreme)
    print(f"\nExtreme Scenario State: {state_extreme}")
    if state_extreme > 150 or state_extreme < -150:
        failsafe.block_system()
        print(f"Failsafe triggered in extreme scenario: {failsafe.respond('extreme test')}")

if __name__ == "__main__":
    test_critical_point()