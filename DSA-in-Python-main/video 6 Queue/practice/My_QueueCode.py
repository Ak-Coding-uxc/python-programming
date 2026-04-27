class Queue:
    def __init__(self):
        self.s = []
    
    def isEmpty(self):
        return len(self.s) == 0

    def enqueLast(self,value):
        self.s.append(value)

    def dequeFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            self.s.pop(0)
    
    def printf(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            for x in self.s:
                print(x , end = " ")
            print()

q = Queue()
q.enqueLast(100)
q.enqueLast(200)
q.enqueLast(300)
q.enqueLast(400)
q.enqueLast(500)

q.printf()
q.dequeFront()
q.printf()
q.dequeFront()
q.printf()
q.dequeFront()
q.printf()
q.dequeFront()
q.printf()
q.dequeFront()
q.printf()

