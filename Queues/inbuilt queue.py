# inbuilt queue
import queue

q = queue.Queue()
q.put(1)    #enqueue
q.put(2)
q.put(3)
q.put(40)
print("length of queue:", q.qsize())
print(q.empty())   #returns True if queue is empty, False is not empty
while not q.empty():
    print(q.get())  # it will dequeue and return the value
