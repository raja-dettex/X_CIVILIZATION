import random

from agent import Agent
from world import World
from metrics import MetricsCollector

ENERGY_LOSS_PER_TICK = 1
ENERGY_GAIN_FROM_FOOD = 20

class Simulation:
    def __init__(self, 
        width: int,
        height: int,
        initial_agents: int,
        initial_food: int,
        food_spawn_per_tick: int
    ):
        self.food_spawn_per_tick = food_spawn_per_tick
        self.tick: int = 0
        self.world = World(width, height, initial_food)
        self.metrics = MetricsCollector()
        self.agents = []

        for agent_id in range(initial_agents):
            (x, y) = self.world.random_position()
            self.agents.append(
                Agent(agent_id, x= x, y= y, energy=50)
            )
    def move(self, agent: Agent):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        agent.x = (agent.x + dx) % self.world.width
        agent.y = (agent.y + dy) % self.world.height

    def eat(self, agent: Agent):
        if self.world.consume_food(agent.x, agent.y):
            agent.energy += ENERGY_GAIN_FROM_FOOD

    def update_agent(self, agent: Agent):
         self.move(agent)
         self.eat(agent)
         agent.energy -= ENERGY_LOSS_PER_TICK
         agent.age += 1

    def remove_dead_agents(self):
        self.agents = [agent for agent in self.agents if agent.is_alive()]
        
    def spawn_food(self):
        for _ in range(self.food_spawn_per_tick):
            self.world.spawn_food()


    def collect_metrics(self):
        population = len(self.agents)

        avg_energy = sum(
            agent.energy for agent in self.agents
        ) / population if population > 0 else 0
        
        self.metrics.collect(
            tick=self.tick,
            population=population,
            avg_energy=avg_energy,
            food=self.world.total_food(),
        )

    def step(self):
        self.tick += 1

        self.spawn_food()

        for agent in self.agents:
            self.update_agent(agent)

        self.remove_dead_agents()

        self.collect_metrics()
