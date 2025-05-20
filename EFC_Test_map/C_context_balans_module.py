# Louis Janssens & GitHub Copilot - 19/05/2025

class ContextBalansModule:
    def __init__(self, name="ContextBalans", decay_constant=10):
        self.name = name
        self.balance = 0  # Initial balance value
        self.decay_constant = decay_constant  # Decay constant for gradual return to zero
        self.log = []

    def adjust_balance(self, context):
        """ Adjusts the balance based on the context """
        if context in ["Good", "Light", "positive"]:
            delta = -1
        elif context in ["Bad", "Dark", "negative"]:
            delta = +1
        else:
            delta = -self.balance / self.decay_constant  # Gradual return to zero

        # Update the balance with the new delta, ensuring it stays within the range [-45, 45]
        self.balance = max(-45, min(45, self.balance + delta))

    def get_balance(self):
        """ Returns the current balance """
        return self.balance

    def respond(self, trigger=None):
        """Generate a response based on the current balance."""
        if self.balance < 0:
            response = f"{self.name} responds in a calm (Yin) way."
        else:
            response = f"{self.name} responds in an active (Yang) way."
        self.log.append((trigger, self.balance, response))
        return response