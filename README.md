# Introduction
A task manager that have different functionalities among others, add/delete tasks and save to a json file. Clone this repo to test the project.
# Project Content
```py
Task Manager/
│── main.py                 # Program entry point
│── structures/
│   │── __init__.py         
│   │── linked_list.py      # The linked list for handling tasks
│   │── stack.py            # Undo action (ctrl + z)
│   │── queue.py            # The queue for history
│   │── heap.py             # Binary tree for ordering tasks by priority
│── models/
│   │── __init__.py         
│   │── task.py             # Task class with its attributes
│── utils/
│   │── __init__.py         
│   │── helpers.py          # Auxiliaries functions
│── data/
│   │── tasks.json          # Task storage
│   │── history.json        # History storage
```