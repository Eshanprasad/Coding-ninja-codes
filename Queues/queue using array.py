"""
Queue functionalities
all of the below operations should be O(1)

1. enqueue
2. dequeue
3. size
4. isEmpty
5. front
"""
class QueueUsingArray:
    def __init__(self):
        self.arr = []
        self.count = 0
        self.front_ele = 0
      
    def enqueue(self, data):
        self.arr.append(data)
        self.count += 1
        
    def dequeue(self):
        if self.count==0:
            return -1
        element = self.arr[self.front_ele]
        self.front_ele+=1
        self.count-=1
        return element
        
    def front(self):
        if self.count==0:
            return -1
        return self.arr[self.front_ele]
    
    def size(self):
        return self.count
        
    def isEmpty(self):
        return self.size()==0
