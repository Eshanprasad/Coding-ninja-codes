# inbuilt stack
import queue

q = queue.LifoQueue()       # this is a stack
q.put(10)                   # appends the element to the stack
q.put(20)
q.put(30)
print(q.qsize())            # returns the size of stack
while not q.empty():
    print(q.get())          # removes the element from the stack and returns the value
    
