# Build: 5073208d7a3d5edfd082ac2eb50ded5f

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
