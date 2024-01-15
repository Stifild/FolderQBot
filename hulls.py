class Quest:
    def __init__(self):
        pass

class Error:
    timing: int
    damage: int

    def __init__(self, timing, damage):
        self.timing = timing
        self.damage = damage
