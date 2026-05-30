class MetricsCollector:
    def __init__(self):
        self.data = []

    def collect(self,
        tick: int, 
        population: int,
        avg_energy: float,
        food: int 
    ):
        self.data.append({
            "tick": tick,
            "population": population,
            "avg_energy": avg_energy,
            "food": food
        })

    def latest(self):
        return self.data[-1]
    
    def reset(self):
        self.data = []
        