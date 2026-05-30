from world import Season


CONFIG = {
    "width": 100,
    "height": 100,
    "initial_agents": 100,
    "initial_food": 500,
    "food_spawn_per_tick": 10,
    "ticks": 5000,
}

SEASONAL_FOOD = {
    Season.SPRING: 8,
    Season.SUMMER: 6,
    Season.AUTUMN: 4,
    Season.WINTER: 1,
}