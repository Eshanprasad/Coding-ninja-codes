"""
Queue functionalities
all of the below operations should be O(1)

1. enqueue
2. dequeue
3. size
4. isEmpty
5. front
"""
#my attempt
class Queue:
    def __init__(self):
        self.arr = []
        self.front_ele = None
        self.length = 0

    def enqueue(self, ele):
        self.arr.append(ele)
        self.length+=1
        if self.front_ele is None:
            self.front_ele = 0


    def isEmpty(self):
        return self.length==0

    def size(self):
        return self.length

    def dequeue(self):
        if self.length<=1:
            self.front_ele = None
        else:
            self.front_ele+=1
        if self.length!=0:
            self.length-=1
    def front(self):
        if self.length!=0:
            return self.arr[self.front_ele]
        return None
