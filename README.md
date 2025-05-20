# EFC Sentiment Analysis Project

*Louis Janssens & GitHub Copilot – 19/05/2025*

This project is a modular, extensible EFC (Emotion-Focused Computing) architecture for sentiment analysis, emotion detection, and AI context balance. It combines text, audio, and image analysis with failsafe mechanisms and a core computation.

## Project structure

```

EFC_module_overhaull
├── A_sentiment_analysis.py # Emotion detection (text/audio/image)
├── B_core_module.py # Central control (CoreModule)
├── C_context_balans_module.py # ContextBalanceModule (Yin/Yang)
├── D_context_situation_controle.py # ContextSituationControlModule
├── E_primaire_secondarie_basicneeds.py # PrimarySecondaryBasicNeedsModule
├── F_calculate_module.py # Core calculation (calculate_core)
├── G_failsafe_module.py # Failsafe & oversight modules
└── README.md # Project documentation

```

## Installation

Clone this repository and install the required dependencies (if necessary):

'''bash
pip install -r requirements.txt
```

## Usage

**Example: Basic sentiment analysis**

'''python
from A_sentiment_analysis import detect_emotion_text

text = "I'm so happy and happy today."
emotion = detect_emotion_text(text)
print(f"Detected emotion: {emotion}")
```

**Example: Full EFC core flow**

'''python
from B_1core_module import CoreModule

core = CoreModule()
core.process_text("I'm so happy and happy today.")
```

## Testing

The test files for the EFC system can be found in the 'Z_testing_files' folder.  

**Please note:**  

- Always copy the desired test file to the "EFC_Test_map" folder before you run it.
- To avoid import conflicts, make sure that there is never more than one test file in 'EFC_Test_map' at a time.
- Perform the test with, for example:
  '''bash
  python EFC_Test_map\AA_test_Overhaull.py
  ```

## Features

- **Modular:** Each module has its own responsibility.
- Extensible: Easily add new analytics or failsafe modules.
- Failsafe: Oversight module can block the entire system in the event of an emergency.
- **Multi-input:** Support for text, audio and image (audio/image as placeholder).
- Core calculation: Combines outputs from all modules into one core value.

## Contributions

Contributions are welcome! Open an issue or pull request for improvements or bug fixes.

## License

MIT License. See LICENSE for details.

---
*Made by Louis Janssens & GitHub Copilot – 19/05/2025*
