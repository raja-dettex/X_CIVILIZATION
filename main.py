from simulation import Simulation
from experiments.baseline import CONFIG


def main():
    sim = Simulation(
        width=CONFIG["width"],
        height=CONFIG["height"],
        initial_agents=CONFIG["initial_agents"],
        initial_food=CONFIG["initial_food"],
        food_spawn_per_tick=CONFIG["food_spawn_per_tick"],
    )

    for _ in range(CONFIG["ticks"]):
        sim.step()

        if sim.tick % 100 == 0:
            m = sim.metrics.latest()

            print(
                f"[Tick={m['tick']}] "
                f"Population={m['population']} "
                f"Food={m['food']} "
                f"AvgEnergy={m['avg_energy']:.2f}"
            )

        if len(sim.agents) == 0:
            print(f"Extinction at tick {sim.tick}")
            break


if __name__ == "__main__":
    main()