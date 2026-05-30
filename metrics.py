from re import M


class MetricsCollector:
    def __init__(self):
        self.data = []

    def collect(self,
        tick: int, 
        population: int,
        avg_energy: float,
        food: int,
        food_rotted: int,
        food_eaten: int, 
        new_agents: int,
        dead_agents: int
    ):
        self.data.append({
            "tick": tick,
            "population": population,
            "avg_energy": avg_energy,
            "food": food,
            "food_rotted" : food_rotted,
            "food_eaten": food_eaten,
            "new_agents": new_agents,
            "dead_agents": dead_agents
        })

    def latest(self):
        return self.data[-1]
    
    def reset(self):
        self.data = []
        