# Louis Janssens & GitHub Copilot - 19/05/2025

class PrimaireSecondaireBasicNeedsModule:
    def __init__(self, alpha, beta, gamma):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.name = "PrimaireSecondaireBasicNeeds Module"

    def behoefte_voldoening(self, behoeften):
        return sum(behoeften)

    def bereken_P(self, primaire_behoeften, secundaire_behoeften, basic_needs):
        P = (
            self.alpha * self.behoefte_voldoening(primaire_behoeften)
            + self.beta * self.behoefte_voldoening(secundaire_behoeften)
            + self.gamma * self.behoefte_voldoening(basic_needs)
        )
        return P

    def some_functionality(self):
        print(f"{self.name} is performing some functionality.")
        return self.bereken_P([0.8, 0.9, 0.7], [0.6, 0.5, 0.4], [1.0, 0.9])  # Example values
