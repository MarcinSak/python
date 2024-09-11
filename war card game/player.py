class Player():
    def __init__(self, name: str) -> Player:
        self.name = name
    def __str__(self) -> str:
        return f"{self.name}"
