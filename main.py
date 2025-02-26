import json
import time
from storage.save_load import load_world, save_world
from interface.cli_dashboard import run_cli
from world.environment import Environment
from agents.human import Human
from agents.animal import Animal

# Load previous state or start fresh
world_state = load_world()

def main():
    print("\n🌍 SaneGenesis Evolution: AI-Driven Society Simulation\n")
    
    if not world_state:
        print("🔄 No previous state found. Creating a new world...")
        world = Environment()
        world.populate()  # Generate initial agents
    else:
        print("✅ Resuming from last saved state...")
        world = Environment.load_from_state(world_state)
    
    try:
        run_cli(world)
    except KeyboardInterrupt:
        print("\n💾 Saving world state before exit...")
        save_world(world)
        print("✅ Simulation saved successfully. Exiting...")

if __name__ == "__main__":
    main()
