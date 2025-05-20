# EFC Sentiment Analysis Project

*Louis Janssens & GitHub Copilot – 19/05/2025*

Dit project is een modulaire, uitbreidbare EFC (Emotion-Focused Computing) architectuur voor sentimentanalyse, emotiedetectie en AI-contextbalans. Het combineert tekst, audio en beeldanalyse met failsafe-mechanismen en een kernberekening.

## Projectstructuur

```

EFC_module_overhaull
├── A_sentiment_analysis.py                # Emotiedetectie (tekst/audio/beeld)
├── B_1core_module.py                      # Centrale aansturing (CoreModule)
├── C_context_balans_module.py             # ContextBalansModule (Yin/Yang)
├── D_context_situation_controle.py        # ContextSituationControlModule
├── E_primaire_secondarie_basicneeds.py    # PrimaireSecondaireBasicNeedsModule
├── F_calculate_module.py                  # Kernberekening (calculate_core)
├── G_failsafe_module.py                   # Failsafe & oversight modules
└── README.md                              # Projectdocumentatie

```

## Installatie

Clone deze repository en installeer de vereiste dependencies (indien nodig):

```bash
pip install -r requirements.txt
```

## Gebruik

**Voorbeeld: basis sentimentanalyse**

```python
from A_sentiment_analysis import detect_emotion_text

text = "Ik ben zo blij en gelukkig vandaag."
emotion = detect_emotion_text(text)
print(f"Detected emotion: {emotion}")
```

**Voorbeeld: volledige EFC-core flow**

```python
from B_1core_module import CoreModule

core = CoreModule()
core.process_text("Ik ben zo blij en gelukkig vandaag.")
```

## Testen

De testbestanden voor het EFC-systeem vind je in de map `Z_testing_files`.  

**Let op:**  

- Kopieer steeds het gewenste testbestand naar de map `EFC_Test_map` voordat je het uitvoert.
- Zorg dat er nooit meer dan één testbestand tegelijk in `EFC_Test_map` staat om importconflicten te voorkomen.
- Voer de test uit met bijvoorbeeld:
  ```bash
  python EFC_Test_map\AA_test_Overhaull.py
  ```

## Features

- **Modulair:** Elke module heeft een eigen verantwoordelijkheid.
- **Uitbreidbaar:** Voeg eenvoudig nieuwe analyse- of failsafe-modules toe.
- **Failsafe:** Oversight-module kan het hele systeem blokkeren bij nood.
- **Multi-input:** Ondersteuning voor tekst, audio en beeld (audio/beeld als placeholder).
- **Kernberekening:** Combineert outputs van alle modules tot één kernwaarde.

## Bijdragen

Bijdragen zijn welkom! Open een issue of pull request voor verbeteringen of bugfixes.

## Licentie

MIT License. Zie LICENSE voor details.

---
*Gemaakt door Louis Janssens & GitHub Copilot – 19/05/2025*