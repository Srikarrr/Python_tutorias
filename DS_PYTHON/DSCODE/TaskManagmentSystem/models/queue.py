from collections import deque

class queue:
      def __init__(self):
           self.items=deque()

      def enqueue(self,item):
             self.items.append(item)

      def dequeue(self):
             self.items.popleft()

      def is_empty(self):
           return len(self.items) == 0                     