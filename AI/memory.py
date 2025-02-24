import json

class Memory:
    def __init__(self, file_path="storage/data/agent_memory.json"):
        self.file_path = file_path
        self.memory_data = self.load_memory()

    def load_memory(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_memory(self):
        with open(self.file_path, "w") as file:
            json.dump(self.memory_data, file, indent=4)

    def update_memory(self, agent_id, memory_entry):
        if agent_id not in self.memory_data:
            self.memory_data[agent_id] = []
        self.memory_data[agent_id].append(memory_entry)
        self.save_memory()
