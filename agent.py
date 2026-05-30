from dataclasses import dataclass

@dataclass
class Agent:
    id: int
    x: int
    y: int
    energy: float
    age: int = 0
    def is_alive(self) -> bool:
        return self.energy > 0