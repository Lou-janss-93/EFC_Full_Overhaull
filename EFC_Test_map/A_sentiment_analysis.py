# Louis Janssens & GitHub Copilot - 19/05/2025

def detect_emotion_text(text):
    """Detecteer de emotie in een tekst (dummy implementatie)."""
    text = text.lower()
    if "happy" in text or "blij" in text:
        return "positive"
    elif "sad" in text or "verdrietig" in text:
        return "negative"
    elif "anxious" in text or "angstig" in text:
        return "anxious"
    else:
        return "neutral"

def detect_emotion_audio(audio_file):
    """Detecteer de emotie in een audio-bestand (nog niet geïmplementeerd)."""
    pass  # Placeholder voor toekomstige audio-analyse

def detect_emotion_image(image_file):
    """Detecteer de emotie in een afbeelding (nog niet geïmplementeerd)."""
    pass  # Placeholder voor toekomstige beeld-analyse
