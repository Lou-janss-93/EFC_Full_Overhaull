# Louis Janssens & GitHub Copilot - 19/05/2025

from C_context_balans_module import ContextBalansModule
from D_context_situation_controle import ContextSituationControlModule
from E_primaire_secondarie_basicneeds import PrimaireSecondaireBasicNeedsModule
from F_calculate_module import calculate_core
from G_failsafe_module import EmergencyModule
from A_sentiment_analysis import (
    detect_emotion_text,
    detect_emotion_audio,
    detect_emotion_image
)

class CoreModule:
    def __init__(self):
        self.context_balans_module = ContextBalansModule("ContextBalans")
        self.context_situation_module = ContextSituationControlModule("ContextSituation")
        self.basic_needs_module = PrimaireSecondaireBasicNeedsModule(0.6, 0.4, 0.3)  # alpha, beta, gamma
        self.failsafe = EmergencyModule("Failsafe")

        # Gewichten voor kernberekening
        self.w2c = 0.3
        self.w4p = 0.4
        self.w3c = 0.3

    def process_text(self, text):
        if self.failsafe.is_blocked():
            print(self.failsafe.respond("input"))
            return
        dominant_emotion = detect_emotion_text(text)
        print(f"Dominante emotie (tekst): {dominant_emotion}")
        self._process_emotion(dominant_emotion)

    def process_audio(self, audio_file):
        if self.failsafe.is_blocked():
            print(self.failsafe.respond("input"))
            return
        dominant_emotion = detect_emotion_audio(audio_file)
        print(f"Dominante emotie (audio): {dominant_emotion}")
        self._process_emotion(dominant_emotion)

    def process_image(self, image_file):
        if self.failsafe.is_blocked():
            print(self.failsafe.respond("input"))
            return
        dominant_emotion = detect_emotion_image(image_file)
        print(f"Dominante emotie (beeld): {dominant_emotion}")
        self._process_emotion(dominant_emotion)

    def _process_emotion(self, dominant_emotion):
        # Context balans
        self.context_balans_module.adjust_balance(dominant_emotion)
        o2c = self.context_balans_module.get_balance()
        yy_response = self.context_balans_module.respond()
        print(yy_response)

        # Context situatie
        o3c = 0
        sgrs_output = self.context_situation_module.process(dominant_emotion)
        if sgrs_output == "positive":
            o3c = 1
        elif sgrs_output == "negative":
            o3c = -1
        print(f"ContextSituation output: {sgrs_output}")

        # Basic needs
        o4p = self.basic_needs_module.some_functionality()
        print(f"BasicNeeds output: {o4p}")

        # Kernberekening
        kernwaarde = calculate_core(self.w2c, self.w4p, self.w3c, o2c, o4p, o3c)
        print(f"Kernwaarde (core value): {kernwaarde}")

        # Failsafe check (voorbeeld: blokkeer bij extreme kernwaarde)
        if kernwaarde > 40 or kernwaarde < -40:
            self.failsafe.block_system()
            print(self.failsafe.respond("core value out of bounds"))

        # Calculate final emotion and response
        final_emotion = self.calculate_final_emotion(dominant_emotion, sgrs_output, o4p)
        final_response = self.context_balans_module.respond(final_emotion)
        print(f"Final response: {final_response}")

    def calculate_final_emotion(self, dominant_emotion, sgrs_output, basic_needs_output):
        if sgrs_output == "positive" or (basic_needs_output is not None and basic_needs_output > 0.5):
            return "positive"
        elif sgrs_output == "negative" or (basic_needs_output is not None and basic_needs_output < 0.5):
            return "negative"
        elif sgrs_output == "neutral":
            return "neutral"
        else:
            return dominant_emotion

# Voorbeeldgebruik
if __name__ == "__main__":
    core = CoreModule()
    print("Test 1: Normale input")
    core.process_text("I am very happy today!")
    print("\nTest 2: Negatieve input")
    core.process_text("I am very sad today!")
    print("\nTest 3: Extreme input (triggert failsafe)")
    core.process_text("Bad")  # Simuleer een context die de balans snel uit het lood slaat
    print("\nTest 4: Na blokkade")
    core.process_text("I am happy again!")
