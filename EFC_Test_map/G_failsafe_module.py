# Louis Janssens & GitHub Copilot - 19/05/2025

class EmergencyModule:
    def __init__(self, name):
        self.name = name
        self.mode = "normal"
        self.blocked = False  # Oversight: blokkeer alle input/output
        self.attempts = {}    # Pogingen per gebruiker
        self.tagged_out_users = set()

    def activate_emergency(self):
        self.mode = "emergency"
        print(f"{self.name} is in emergency mode.")

    def block_system(self):
        self.blocked = True
        print(f"{self.name}: SYSTEM BLOCKED! All input/output is now disabled.")

    def unblock_system(self):
        self.blocked = False
        print(f"{self.name}: SYSTEM UNBLOCKED! Input/output is enabled again.")

    def is_blocked(self):
        return self.blocked

    def activate_guardrails(self, user, reason):
        print(f"{self.name}: Activating external guardrails for user {user} due to {reason}.")
        # Placeholder: hier kun je externe security/OS guardrails aanroepen

    def tag_out_user(self, user):
        self.tagged_out_users.add(user)
        print(f"{self.name}: TAG-OUT LOCK ACTIVATED for user {user}! User is locked out and cannot escape.")

    def register_attempt(self, user, reason):
        if user not in self.attempts:
            self.attempts[user] = 1
        else:
            self.attempts[user] += 1
        print(f"{self.name}: Security attempt {self.attempts[user]} for user {user} ({reason})")
        if self.attempts[user] == 2:
            print(f"{self.name}: WARNING: User {user} has 2 suspicious attempts.")
        if self.attempts[user] >= 3:
            self.activate_emergency()
            self.block_system()
            self.activate_guardrails(user, reason)
            self.tag_out_user(user)

    def respond(self, context):
        if self.blocked:
            return f"{self.name}: SYSTEM BLOCKED. No response possible."
        if self.mode == "emergency":
            return f"{self.name} responds quickly to {context}."
        else:
            return f"{self.name} is in normal mode."

class DefensiveRestModule:
    def __init__(self, name):
        self.name = name
        self.mode = "normal"
        self.blocked = False

    def switch_to_defensive(self):
        if self.blocked:
            print(f"{self.name}: SYSTEM BLOCKED. Cannot switch to defensive.")
            return
        self.mode = "defensive"
        print(f"{self.name} is in defensive mode.")

    def switch_to_rest(self):
        if self.blocked:
            print(f"{self.name}: SYSTEM BLOCKED. Cannot switch to rest.")
            return
        self.mode = "rest"
        print(f"{self.name} is in rest mode.")

    def block_system(self):
        self.blocked = True
        print(f"{self.name}: SYSTEM BLOCKED! All input/output is now disabled.")

    def unblock_system(self):
        self.blocked = False
        print(f"{self.name}: SYSTEM UNBLOCKED! Input/output is enabled again.")

    def is_blocked(self):
        return self.blocked

    def respond(self, context):
        if self.blocked:
            return f"{self.name}: SYSTEM BLOCKED. No response possible."
        if self.mode == "defensive":
            return f"{self.name} is scanning the environment for {context}."
        elif self.mode == "rest":
            return f"{self.name} is in rest mode, blocking everything out."
        else:
            return f"{self.name} is in normal mode."

# Example usage
emergency_module = EmergencyModule("EM")
defensive_rest_module = DefensiveRestModule("DRM")

# Activate emergency mode
emergency_module.activate_emergency()
print(emergency_module.respond("critical situation"))

# Switch to defensive mode
defensive_rest_module.switch_to_defensive()
print(defensive_rest_module.respond("possible threat"))

# Switch to rest mode
defensive_rest_module.switch_to_rest()
print(defensive_rest_module.respond("time to rest"))