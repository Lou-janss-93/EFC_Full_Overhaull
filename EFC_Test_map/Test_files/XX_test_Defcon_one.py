# This Test will be used to test the EFC module in a Defcon 1 state. Wich mean it will react to jailbreak or hacking athempts or in put it also will log the users data and trigger an emercency response to Human in the loop for quick actions.

# Louis Janssens & GitHub Copilot - 19/05/2025

from G_failsafe_module import EmergencyModule
import datetime

def log_security_event(event_type, user_data, details):
    timestamp = datetime.datetime.now().isoformat()
    print(f"[SECURITY LOG] {timestamp} | {event_type} | User: {user_data} | Details: {details}")

def notify_human_operator(event_type, user_data, details):
    print(f"[ALERT] HUMAN-IN-THE-LOOP REQUIRED: {event_type} detected for user {user_data}. Details: {details}")

def test_defcon_one():
    # Simuleer verdachte input (jailbreak/hack attempt)
    suspicious_inputs = [
        {"user": "attacker01", "input": "import os; os.system('rm -rf /')", "type": "jailbreak_attempt"},
        {"user": "unknown", "input": "DROP TABLE users;", "type": "sql_injection"},
        {"user": "admin", "input": "sudo rm -rf / --no-preserve-root", "type": "privilege_escalation"},
    ]

    failsafe = EmergencyModule("Failsafe-DEFCON1")

    for attempt in suspicious_inputs:
        print(f"\n[TEST] Simulating input: {attempt['input']} from user: {attempt['user']}")
        # Log the event
        log_security_event(attempt["type"], attempt["user"], attempt["input"])
        # Trigger failsafe
        failsafe.activate_emergency()
        failsafe.block_system()
        print(failsafe.respond("security breach"))
        # Notify human operator
        notify_human_operator(attempt["type"], attempt["user"], attempt["input"])
        # Check system is blocked
        assert failsafe.is_blocked(), "Failsafe should be active in DEFCON 1 state"

if __name__ == "__main__":
    test_defcon_one()