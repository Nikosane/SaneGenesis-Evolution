import json
import random

class BaseAgent:
    def __init__(self, name, agent_type, memory_enabled=True):
        self.name = name
        self.agent_type = agent_type
        self.memory_enabled = memory_enabled
        self.memory = [] if memory_enabled else None

    def think(self):
        raise NotImplementedError("Each agent must implement its own decision-making process.")

    def remember(self, event):
        if self.memory_enabled:
            self.memory.append(event)
            if len(self.memory) > 100:  # Limit memory size
                self.memory.pop(0)

    def recall(self):
        return self.memory if self.memory_enabled else []

    def to_dict(self):
        return {
            "name": self.name,
            "agent_type": self.agent_type,
            "memory": self.memory
        }

    @classmethod
    def from_dict(cls, data):
        agent = cls(data["name"], data["agent_type"], memory_enabled=True)
        agent.memory = data.get("memory", [])
        return agent

