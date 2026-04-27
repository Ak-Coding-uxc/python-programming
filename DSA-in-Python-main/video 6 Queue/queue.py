class Queue:
    def __init__(self): # self represent object that are we using
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0 # return true if queue is empty
    
    def insert(self,value): # this is called enqueue(insert ko ye bolte h queue mein)
        self.items.append(value) #insert in rear
    
    def delete(self): # called dequeue
        if(len(self.items)== 0):
            raise Exception("Queue is Empty")
        else:
            return self.items.pop(0)
        
    def pri(self):
        if(len(self.items)== 0):
            raise Exception("Queue is Empty")
        else:
            for x in self.items:
                print(x , end = " ")
            print()

q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

q.pri()

print(q.delete())
print(q.delete())
print(q.delete())

q.pri()

# bookmark = 31 minute.