"""
Queue functionalities
all of the below operations should be O(1)

1. enqueue
2. dequeue
3. size
4. isEmpty
5. front
"""
#queue using linkedlist

class LinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = next

class QueueUsingLinkedList:
    def __init__(self):
        self.count = 0
        self.front_node = None
        self.rear_node = None

    def enqueue(self, val):
        newNode = LinkedList(val)
        if self.front_node is None:
            self.front_node = newNode
            self.rear_node = newNode
        else:
            self.rear_node.next = newNode
            self.rear_node = newNode
        self.count += 1

    def dequeue(self):
        if self.count!=0:       # can also use if self.front_node is not None:
            value = self.front_node.val
            self.front_node = self.front_node.next
            self.count-=1
            return value

    def front(self):
        if self.count!=0:       # can also use if self.front_node is not None:
            return self.front_node.val
        
    def isEmpty(self):
        return self.count==0

    def size(self):
        return self.count
