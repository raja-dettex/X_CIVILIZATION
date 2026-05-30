from dataclasses import dataclass

@dataclass
class Agent:
    id: int
    x: int
    y: int
    energy: float
    parent_id: int | None
    vision: int = 3
    age: int = 0
    metabolism: float = 1.0
    def is_alive(self) -> bool:
        return self.energy > 0

from collections import Counter


def species_distribution(agents: [Agent]):
    counter = Counter()
    for agent in agents:
        species = (
            agent.vision,
            round(agent.metabolism, 1)
        )
        counter[species] += 1

    return counter



def vision_distribution(agents):

    return Counter(
        a.vision
        for a in agents
    )