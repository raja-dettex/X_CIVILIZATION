import random


class World:
    def __init__(self, width: int, height: int, initial_food: int):
        self.width = width
        self.height = height

        ## food grid: (x, y) -> food level
        self.food = {}
        for _ in range(initial_food):
            self.spawn_food()


    def random_position(self):
        return (random.randint(0, self.width - 1), random.randint(0, self.height - 1))

    def spawn_food(self):
        (x, y) = self.random_position()

        self.food[(x, y)] = self.food.get((x, y), 0) + 1

    def get_food(self, x: int, y: int) -> int:
        return self.food.get((x, y), 0)

    def consume_food(self, x: int, y: int) -> bool:
        amount = self.food.get((x, y), 0) 

        if amount <= 0:
            return False
        
        if amount == 1:
            del self.food[(x, y)]

        if amount > 1:
            self.food[(x, y)] -= 1

        return True

    def total_food(self) -> int:
        return sum(self.food.values())