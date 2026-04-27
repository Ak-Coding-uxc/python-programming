class CircularQueue:
    def __init__(self,size): # first time mentioning size
        self.size = size # used for modulo
        self.items = [None]*size # size  size variable jitna rahega orr sab mein None value by default chali.
        self.front = self.rear = -1
        # used front and rear. not used append and pop because append insert in last and we don't want this. 
    
    def enqueue(self , value): # insert
        if((self.rear + 1) % self.size == self.front):
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
    
    def dequeue(self):
        if(self.front == -1):
            print("Queue is Empty") 
        elif(self.front == self.rear):
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size

    def printf(self):
        if(self.front == -1):
            print("Queue is Empty")
        else:
            f = self.front
            r = self.rear
            while(f != r):
                print(self.items[f], end = " , ")
                f = (f + 1) % self.size
            print(self.items[f])



    def isEmpty(self):
        if(self.front == -1):
            print("Queue is Empty")
        else:
            print("Queue is not Empty")
    
    def isFull(self):
        if(self.front == -1): # self uss object ke liye joh call kar raha h iss function ko.
            print("Queue is Empty")
        if((rear + 1) % self.size == front):
            print("Yes , Queue is Full")
        else:
            print("No , Queue is not Full")

cq = CircularQueue(5) # size = 5

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)
cq.printf()

cq.dequeue()

cq.printf()

cq.enqueue(60)
cq.enqueue(70)
cq.printf()

cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()



  

        




