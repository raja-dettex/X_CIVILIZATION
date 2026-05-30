import random

from agent import Agent
from world import World
from metrics import MetricsCollector

ENERGY_LOSS_PER_TICK = 1
ENERGY_GAIN_FROM_FOOD = 20
MAX_ENERGY = 100
REPRODUCTION_THRESHOLD = 80
REPRODUCTION_COST = 40
CHILD_START_ENERGY = 40

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
        self.next_agent_id = initial_agents
        self.world = World(width, height, initial_food)
        self.metrics = MetricsCollector()
        self.agents = []
        self.new_agents = 0;
        self.dead_agents = 0;

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
            agent.energy  = min(MAX_ENERGY, agent.energy + ENERGY_GAIN_FROM_FOOD)


    def reproduce(self, agent: Agent) -> Agent:
        if agent.energy < REPRODUCTION_THRESHOLD:
            return None
        agent.energy -= REPRODUCTION_COST

        child = Agent(
            id=self.next_agent_id,
            x=agent.x,
            y=agent.y,
            energy=CHILD_START_ENERGY,
        )

        self.next_agent_id += 1

        return child

    def update_agent(self, agent: Agent):
         self.move(agent)
         self.eat(agent)
         agent.energy -= ENERGY_LOSS_PER_TICK
         agent.age += 1

    def count_dead_agents(self):
        return len([agent for agent in self.agents if not agent.is_alive()])

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
            food_rotted=self.world.food_rotted,
            food_eaten=self.world.food_eaten,
            new_agents = self.new_agents,
            dead_agents = self.dead_agents
        )

    def step(self):
        self.tick += 1
        self.world.age_food()
        self.spawn_food()
        new_agents = []
        for agent in self.agents:
            self.update_agent(agent)
            child = self.reproduce(agent)
            if child:
                new_agents.append(child)
        self.new_agents += len(new_agents)
        self.agents.extend(new_agents)
        self.dead_agents += self.count_dead_agents()
        self.remove_dead_agents()

        self.collect_metrics()
