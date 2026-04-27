class Deque:
    def __init__(self): # self represent object that are we using
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0 # return true if queue is empty
    
    def insertAtEnd(self,value): # this is called enqueue(insert ko ye bolte h queue mein)
        self.items.append(value) #insert in rear
    
    def deleteAtFront(self): # called dequeue
        if(self.isEmpty()):
            raise Exception("Queue is Empty")
        else:
            return self.items.pop(0)

    def insertAtFront(self,value):
        self.items.insert(0,value)

    def deleteAtEnd(self):
        if(self.isEmpty()):
            raise Exception("Queue is Empty")
        else:
            return self.items.pop()

    def pri(self):
        if(self.isEmpty()):
            raise Exception("Queue is Empty")
        else:
            for x in self.items:
                print(x , end = " ")
            print()
    
dq = Deque()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtFront(50)
dq.pri()
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtFront())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())