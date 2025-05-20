# Louis Janssens & GitHub Copilot - 19/05/2025

def calculate_core(w2c, w4p, w3c, o2c, o4p, o3c):
    """Bereken de kern als een gewogen gemiddelde."""
    return (w2c * o2c + w4p * o4p + w3c * o3c) / (w2c + w4p + w3c)
