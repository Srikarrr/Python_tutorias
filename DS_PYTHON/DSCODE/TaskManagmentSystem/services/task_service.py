from models.graph import graph
from models.task import task
from models.queue import queue
from models.stack import stack

class task_service:

       def __init__(self):
           self.tasks = []
           self.task_queue   = queue()
           self.task_history = stack()

       def create_task(self,id,title,description):
           task = task(id,title,description)  
           self.tasks.append(task)
           self.task_queue.enqueue(task)
           return task

       def complete_task(self):
            if not self.task_queue.is_empty() :
                 task = self.task_queue.dequeue()
                 self.task_history.push(task)
                 return task.id,task.title,task.description
            return None  

       def get_task_history(self):
            return self.task_history 


