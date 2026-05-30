import random
from dataclasses import dataclass


FOOD_LIFETIME = 50


@dataclass
class Food:
    amount: int
    age: int = 0


from enum import Enum


class Season(Enum):
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"


class World:
    def __init__(self, width: int, height: int, initial_food: int):
        self.width = width
        self.height = height
        self.food_rotted = 0
        self.food_eaten = 0
        ## food grid: (x, y) -> Food
        self.food: dict[tuple(int, int) , Food] = {}
        for _ in range(initial_food):
            self.spawn_food()


    def random_position(self):
        return (random.randint(0, self.width - 1), random.randint(0, self.height - 1))

    def spawn_food(self):
        (x, y) = self.random_position()
        if (x, y) not in self.food:
            self.food[(x, y)] = Food(amount = 1)
        else:
            self.food[(x,y)].amount += 1
    def age_food(self):
        expired = []
        for pos, food in self.food.items():
            food.age += 1;
            if food.age > FOOD_LIFETIME:
                expired.append(pos)
                self.food_rotted += 1

        for pos in expired:
            del self.food[pos]

    def get_food(self, x: int, y: int) -> int:
        return self.food.get((x, y), 0)


    def find_food_within_radius(self, x: int, y: int, radius: int) -> (int, int):
        nearest = None
        nearest_distance = None
        for (fx, fy), food in self.food.items():
            dx = abs(fx - x)
            dy = abs(fy - y)
            distance = dx + dy
            if distance > radius:
                continue
            if nearest is None or distance < nearest_distance:
                nearest = (fx, fy)
                nearest_distance = distance
        return nearest


    def consume_food(self, x: int, y: int) -> bool:
        if (x,y) not in self.food:
            return False
        amount = self.food[(x,y)].amount

        if amount <= 0:
            return False
        
        if amount == 1:
            self.food_eaten += 1
            del self.food[(x, y)]

        if amount > 1:
            self.food_eaten += 1
            self.food[(x, y)].amount -= 1

        return True

    def total_food(self) -> int:
        return sum([food.amount for food in self.food.values()])