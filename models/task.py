from utils.helpers import generate_task_id

class Task:
    def __init__(self, name, description, priority, limit_date, completed=False, task_id=False):
        self.task_id = task_id if task_id else generate_task_id()    # Generate ID with 8 chars
        self.name = name
        self.desc = description
        self.priority = priority
        self.date = limit_date
        self.completed = completed
        
    def __lt__(self, other): # Defines the comparation of tasks based on priority
        return self.priority < other.priority