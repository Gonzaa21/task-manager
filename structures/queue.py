import json
from collections import deque
from utils.helpers import remove_ansi_codes

class Queue:
    def __init__(self):
        self.queue = deque() # Empty queue
        self.load_history() # Load JSON history
        
    def add_history(self, action):
        if action not in self.queue:
            self.queue.append(action) # Add action to history
    
    def view_history(self):
        if not self.queue:
            print("\033[33m⚠ No actions in history.\033[0m")
            return
        
        print("\n\033[36m📜 Action History:\033[0m")
        for i, action in enumerate(self.queue, 1):
            clean_action = remove_ansi_codes(action)
            if "Completed task" in clean_action:
                print(f"{i}. 📌 {action}")  
            elif "Added task" in clean_action:
                print(f"{i}. ➕ {action}")
            else:
                print(f"{i}. 🔻 {action}")
    
    def save_history(self,): # Save in json
        with open("data\\history.json", "w") as file:
            json.dump(list(self.queue), file, indent=4)
        
    def load_history(self): # Load json file
        try:
            with open("data\\history.json", "r") as file:
                history = json.load(file)
                self.queue = deque(history)
                
        except (FileNotFoundError, json.JSONDecodeError):
            self.queue = deque()