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
        dead_agents: int,
        avg_age: int,
        avg_vision: int,
        max_vision: int,
        min_vision: int,
        avg_metabolism: int,
        season: str
    ):
        self.data.append({
            "tick": tick,
            "population": population,
            "avg_energy": avg_energy,
            "food": food,
            "food_rotted" : food_rotted,
            "food_eaten": food_eaten,
            "new_agents": new_agents,
            "dead_agents": dead_agents,
            "avg_age": avg_age,
            "avg_vision" : avg_vision,
            "min_vision" : min_vision,
            "max_vision" : max_vision,
            "avg_metabolism" : avg_metabolism,
            "current_season" : season
        })

    def latest(self):
        return self.data[-1]
    
    def reset(self):
        self.data = []
        