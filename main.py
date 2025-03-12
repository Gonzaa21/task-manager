import time
from structures.linked_list import LinkedList
from structures.stack import Stack
from utils.helpers import validate_date
from models.task import Task

class Main:
    def __init__(self):
        self.linked_list = LinkedList()
        self.linked_list.load_task()
        self.stack = Stack()
    
    def view_menu(self):
        while True:
            print(f'\033[92m1. Add Task\033[0m')
            print(f'\033[36m2. View pending tasks\033[0m')
            print(f'\033[32m3. Complete task\033[0m')
            print(f'\033[34m4. History\033[0m')
            print(f'\033[33m5. Undo last action\033[0m')
            print(f'\033[31m6. Exit\033[0m')
            
            try:
                select = int(input(f'\033[90mSelect an option: \033[0m'))
                
                if select == 1:
                    print(f'\033[32mAdding new task...\033[0m')
                    time.sleep(2)
                    self.add_task()
                    time.sleep(1)
                    
                elif select == 2:
                    print(f'\033[96mViewing pending tasks...\033[0m')
                    time.sleep(2)
                    self.linked_list.view_tasks()
                    time.sleep(1)
                    
                elif select == 3:
                    print(f'\033[92mCompleting new task...\033[0m')
                    time.sleep(2)
                    self.linked_list.complete_task()
                    time.sleep(1)
                    
                elif select == 4:
                    print(f'\033[94mViewing history...\033[0m')
                    time.sleep(2)
                    self.linked_list.queue.view_history()
                    time.sleep(1)
                    
                    
                elif select == 5:
                    print(f'\033[93mUndoing last action...\033[0m')
                    time.sleep(2)
                    self.linked_list.stack.undo_action()
                    time.sleep(1)
                    
                elif select == 6:
                    print(f'\033[91mBye!\033[0m')
                    break
                
                else:
                    print(f'\033[31mInvalid option, try again.\033[0m')
                
            except Exception as e:
                print(f'\033[31mInvalid action, try again.\033[0m ERROR: {e}')
    
    def add_task(self):
        name = input(f"\033[90mEnter task title:\n>> ")
        description = input(f"\033[90mEnter task description:\033[0m\n>> ")
        
        # validations
        while True:
            priority = int(input(f"\033[90mEnter priority (1-10):\033[0m\n>> "))
            try:
                if 1 <= priority <= 10:
                    break
                else:
                    print(f'\033[31mInvalid priority format\033[0m')
            except:
                print(f'\033[31mInvalid action, try again.\033[0m')

        while True:
            limit_date = input(f"\033[90mEnter due date (YYYY-MM-DD):\033[0m\n>> ")
            if validate_date(limit_date):
                break  # if the format is valid, break the loop
            else:
                print(f'\033[31mInvalid date format\033[0m')
        
        task = Task(name, description, priority, limit_date)  # create object Task
        self.linked_list.add_task(task)  # add task to linked list
        self.linked_list.save_task()
        
        print(f"\033[32m✅ Task '{name}' added successfully!\033[0m")
        
# Iterating class
if __name__ == "__main__":
    main = Main()
    main.view_menu()