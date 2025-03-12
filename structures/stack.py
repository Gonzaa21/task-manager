import json
from structures.queue import Queue

class Stack:
    def __init__(self):
        self.stack = [] # Empty stack
        self.queue = Queue()
        
    def push_action(self, action):
        self.stack.append(action) # Add action to stack
        
    def pop_action(self):
        if not self.is_empty(): # If stack is not empty, delete the last action
            return self.stack.pop()
        return None
        
    def is_empty(self):
        return len(self.stack) == 0

    def undo_action(self):
        # If stack is empty...
        if self.is_empty():
            print('\033[33m⚠ No actions to undo.\033[0m')
            return
        
        last_task = self.pop_action() # Obtain the last task added/completed
        
        # Load tasks
        with open("data\\tasks.json", "r") as file:
            tasks = json.load(file)
            
        found = False
        
        
        for task in tasks:
            if task["task_id"] == last_task.task_id:
                if task["completed"]:
                    task["completed"] = False
                    print(f"\033[31m⏪ Task '{task['name']}' marked as pending again!\033[0m")
                    # Save to history
                    self.queue.add_history(f"\033[31m Remove completed task: {task['name']}\033[0m")
                    self.queue.save_history()
                else:
                    # If the task not be completed, will be deleted
                    tasks = [t for t in tasks if t["task_id"] != last_task.task_id] # Filter the task and remove
                    print(f"\033[31m⏪ Task '{task['name']}' removed!\033[0m")
                    # Save to history
                    self.queue.add_history(f"\033[31m Deleted task: {task['name']}\033[0m")
                    self.queue.save_history()
                found = True
                break
            
        # If not exist the task
        if not found:
            print("\033[33m⚠ Task not found in JSON.\033[0m")
            return
        
        # Save changes in json
        with open("data\\tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)