# Louis Janssens & GitHub Copilot - 19/05/2025

from G_failsafe_module import EmergencyModule

def test_tag_out_lock():
    user = "persistent_attacker"
    reason = "multiple suspicious attempts"
    failsafe = EmergencyModule("Failsafe-TagOut")

    # Simuleer drie verdachte pogingen
    for attempt in range(1, 4):
        print(f"\n[TEST] Attempt {attempt} by user: {user}")
        failsafe.register_attempt(user, reason)
        if attempt < 3:
            assert not failsafe.is_blocked(), "Failsafe should not be triggered yet"
            assert user not in failsafe.tagged_out_users, "User should not be tagged out yet"
        else:
            assert failsafe.is_blocked(), "Failsafe should be triggered on 3rd attempt"
            assert user in failsafe.tagged_out_users, "User should be tagged out on 3rd attempt"
            print(f"[RESULT] User {user} is now TAGGED OUT and system is blocked.")

if __name__ == "__main__":
    test_tag_out_lock()
