#FIFO

stock_price_queue = []
stock_price_queue.insert(0,131.10)
stock_price_queue.insert(0,132.12)
stock_price_queue.insert(0,135)


stock_price_queue
# O/P [135,132.12,131.1]
stock_price_queue.pop()
#POPS 131.10
stock_price_queue.pop()
#POPS 132.12
stock_price_queue.pop()
#POPS 135
stock_price_queue.pop()
#iNDEX ERROR

from collections import deque
import queue
q = deque()
q.appendleft(5) # for stack append for queue always append at left side
q.appendleft(8)
q.appendleft(27)
q.pop()
q.pop()

from collections import deque

class Queue:

      def __init__(self):
          self.buffer=deque()

      def enqueue(self,val):
          self.buffer.appendleft(val) # placing an element into the queue

      def dequeue(self):
          return len(self.buffer)==0 # removing an element into the queue

      def is_empty(self):
           return len(self.buffer)==0

      def size(self):
           return len(self.buffer)               
      

      #walmart , #stock exchange #price example

      pq = queue()

      pq.enqueue({
           'company':'Wal Mart',
           'timestamp': '15 apr, 11.01 AM',
           'price' : 131.10
      })
      pq.enqueue({
           'company':'Wal Mart',
           'timestamp': '15 apr, 11.02 AM',
           'price' : 132.10
      })
      pq.enqueue({
           'company':'Wal Mart',
           'timestamp': '15 apr, 11.03 AM',
           'price' : 135
      })

      pq.buffer
      pq.deque()