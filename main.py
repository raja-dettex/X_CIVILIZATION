from simulation import Simulation
from experiments.baseline import CONFIG
from agent import species_distribution, vision_distribution


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
            species = species_distribution(sim.agents)

            print("\nTop Species")

            for genotype, count in species.most_common(10):
                print(
                    f"{genotype} -> {count}"
                )
            vision_dist = vision_distribution(
                sim.agents
            )

            print("\nVision Distribution")

            for vision in sorted(
                vision_dist.keys()
            ):
                print(
                    f"{vision}: "
                    f"{vision_dist[vision]}"
                )
            print(
                f"[Tick={m['tick']}] "
                f"Population={m['population']} "
                f"Food={m['food']} "
                f"AvgEnergy={m['avg_energy']:.2f} "
                f"FoodRotted={m['food_rotted']} "
                f"FoodEaten={m['food_eaten']} "
                f"NewAgents={m['new_agents']} "
                f"DeadAgents={m['dead_agents']} "
                f"AvgAge={m['avg_age']} "
                f"AvgVision={m['avg_vision']:.2f} "
                f"VisionRange=({m['min_vision']},{m['max_vision']}) "
                f"AvgMetabolism={m['avg_metabolism']} ",
                f"CurrentSeason={m['current_season']}"
            )

        if len(sim.agents) == 0:
            print(f"Extinction at tick {sim.tick}")
            break


if __name__ == "__main__":
    main()