import time
import random
from rich.console import Console
from rich.table import Table

console = Console()

def display_dashboard(agents, world):
    table = Table(title="🌍 SaneGenesis Evolution - Live Simulation")
    table.add_column("Agent", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Last Action", style="green")

    for agent in agents:
        table.add_row(agent.name, agent.agent_type, random.choice(["Exploring", "Trading", "Fighting", "Evolving"]))

    console.clear()
    console.print(table)
    console.print(f"\n🌤 Weather: {world.weather} | 🌱 Resources: {world.resources}\n", style="bold yellow")
    
    time.sleep(1)
