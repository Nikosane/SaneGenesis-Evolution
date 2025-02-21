CONFIG = {
    "simulation_speed": 1.0,  # Speed multiplier for time progression
    "logging": {
        "enable": True,
        "log_file": "simulation.log"
    },
    "world": {
        "size": 100,  # Grid size of the environment
        "resource_abundance": 1.5  # Multiplier for resource generation
    },
    "agents": {
        "initial_population": 10,
        "memory_persistence": True  # Save agent decisions & personality
    }
}
