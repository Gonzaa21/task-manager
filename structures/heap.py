import heapq
from models.task import Task

class Heap:
    def __init__(self):
        self.heap = [] # Heap empty
        
    def push_heap(self, task:Task): # Instert and order by priority
        heapq.heappush(self.heap, (task.priority, task))
    
    def pop_heap(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]  # Return only the task
        return None
    
    def sort_heap(self): # Extract the order tasks and returns a list
        return [task for _, task in sorted(self.heap)]