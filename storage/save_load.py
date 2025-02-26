import json
import os

class SaveLoad:
    def __init__(self, file_path="storage/data/world_state.json"):
        self.file_path = file_path

    def save_state(self, state):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w") as file:
            json.dump(state, file, indent=4)
        print("[SAVE] World state saved successfully.")

    def load_state(self):
        if not os.path.exists(self.file_path):
            print("[LOAD] No saved world state found. Starting fresh.")
            return None
        
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("[ERROR] Corrupted world state file. Starting fresh.")
            return None
