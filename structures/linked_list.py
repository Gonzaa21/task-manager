import json
from models.task import Task
from structures.heap import Heap
from structures.queue import Queue
from structures.stack import Stack

# Node class
class Node:
    def __init__(self, task: Task):
        self.task = task
        self.next = None

# linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        
        self.heap = Heap()
        self.queue = Queue()
        self.stack = Stack()
        
    def add_task(self, task: Task, add_to_history=True):
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node
        
        # Heap
        self.heap.push_heap(task) # add task to heap
        
        # Queue
        if add_to_history:
            self.queue.add_history(f"\033[32mAdded task: {task.name}\033[0m")
            self.queue.save_history()
        
        # Stack
        self.stack.push_action(task)
        
    def view_tasks(self):
        sort_heap = self.heap.sort_heap()  # Obtain order tasks by priority
        
        if not sort_heap:
            print("\033[33m⚠ No tasks found.\033[0m")
            return

        for task in sort_heap:
            print(f"======================\n\033[36mTask ID°{task.task_id}\033[0m\n======================\n"
                  f"\033[94m📌 Title: \033[0m{task.name}\n"
                  f"\033[94m📄 Description: \033[0m{task.desc}\n"
                  f"\033[94m⚡ Priority: \033[0m{task.priority}\n"
                  f"\033[94m📅 Due Date: \033[0m{task.date}\n"
                  f"\033[94m🔘 Status: \033[0m{'✅ Completed' if task.completed else '⏳ Pending'}\n")

    def save_task(self):
        tasks = []
        current = self.head
        while current:
            tasks.append({
                "task_id":current.task.task_id,
                "name": current.task.name,
                "description": current.task.desc,
                "priority": current.task.priority,
                "limit_date": current.task.date,
                "completed": current.task.completed
            })
            current = current.next
        
        with open("data\\tasks.json", "w") as file:
            json.dump(tasks, file, indent=4) # convert py objects to json
    
    def load_task(self):
        with open("data\\tasks.json", "r") as file:
            content = file.read().strip()  # Delete blank spaces

            if not content:  # if archive is empty, create empty array
                print("\033[33m⚠ No tasks found.\033[0m")
                return
            
            tasks = json.loads(content)
            for task_data in reversed(tasks):  # keep order
                task = Task(**task_data)
                self.add_task(task, add_to_history=False)
    
    def complete_task(self):
        task_id = input('\033[32mTask ID to mark as completed: \033[0m').strip()
        try:
            # Load tasks in tasks.json
            with open("data\\tasks.json", "r") as file:
                tasks = json.load(file)

            found = False
            
            # Search task for id and update
            for task in tasks:
                if task["task_id"] == task_id:
                    task["completed"] = True
                    task_name = task["name"]
                    found = True
                    # Stack
                    self.stack.push_action(Task(**task))
                    break
                
            # if found is true, mark as completed.
            if found:
                with open("data\\tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)  # save changes
                print("\033[32m✅ Task marked as completed!\033[0m")
                
                # Queue history
                self.queue.add_history(f"\033[34mCompleted task: {task_name}\033[0m")
                self.queue.save_history()
                
            else:
                print("\033[33m⚠ Task ID not found.\033[0m")

                # Update changes in json
                with open("data\\tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)
        except:
            print('\033[31mInvalid task ID\033[0m')