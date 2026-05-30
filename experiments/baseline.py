from world import Season


CONFIG = {
    "width": 50,
    "height": 50,
    "initial_agents": 100,
    "initial_food": 500,
    "food_spawn_per_tick": 10,
    "ticks": 20000,
}

SEASONAL_FOOD = {
    Season.SPRING: 8,
    Season.SUMMER: 7,
    Season.AUTUMN: 6,
    Season.WINTER: 4,
}