
def pick_outline_width(diameter) -> int:
    if diameter < 300:
        return int(diameter * 0.1)
    if diameter < 600:
        return int(diameter * 0.05)
    return int(diameter * 0.03)