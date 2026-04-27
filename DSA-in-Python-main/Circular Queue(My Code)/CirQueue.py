# Circular queue using linked list

class Node:
    def __init__(self ,value, next = None):
        self.data = value
        self.next = next

class CircularQueue:
    def __init__(self,head = None):
        self.head = head
    
    def enqueLast(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            self.head.next = temp
        else:
            t = self.head
            while(t.next != self.head):
                t = t.next
            t.next = temp
            temp.next = self.head #  point last to first

    def dequeFirst(self):
        if(self.head == None):
            print("Queue is Empty")
        else:
            t = self.head
            if(t.next == self.head):
                self.head = None
            else:
                while(t.next != self.head):
                    t = t.next # to point [t] in last node
                self.head = self.head.next
                t.next = self.head

    def display(self):
        if(self.head == None):
            print("Queue is Empty")
        else:
            t = self.head
            while(t.next != self.head):
                print(t.data , end = " ")
                t = t.next # ha ha ha ( i miss this line) # code go in infinite mode
            print(t.data)

q = CircularQueue()
q.enqueLast(100)
q.enqueLast(200)
q.enqueLast(300)
q.enqueLast(400)

q.display()

q.dequeFirst()
q.dequeFirst()
q.dequeFirst()
q.dequeFirst()
q.dequeFirst()
q.display()

        

        