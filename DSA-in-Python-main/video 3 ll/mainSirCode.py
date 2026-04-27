""" 
TOPIC => singly LINKED LIST
spotify used linked list
web browser also 
masterji.co practice
arange and linspace

linked list allow declare memory at runtime
ARRAY Have continous memoryy  location
linked list not in continous memory location

linked list use node
node have 2 partition
>first is info or data value 
>second is address part to store memory address of next node
pointer or reference model are same 
but python don't have pointer
pointer is a variable which point to an location or an address

construction is used to create object.
last node not point anywhere

advatage => expand kitna bhi

single ll travel in  only 1 direction

my mind question :-= how to store address in python
 """
# we make class because we have to make our own data type
# Memory allocation ke liye init function use hota h jo constructin ki tarah kaaam karta hai
# self ek pointer ki tarah hai jo address store karega
        #info , next hame kya - kya rakhna h wo bataege.(parameters) , none is by default value if any value not given then put None value.
        # not need to declare self.data
        # init function automatically called when new object is created from the class.
class Node: 
    def __init__(self, info, next = None): 
        self.data = info 
        self.next = next

class SinglyLinkedlist:
    def __init__(self,head=None):
        self.head = head

    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtStart(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMiddle(self , value ,x):# loc = location where to insert, ex: 2 ke baad etc or x ke baad
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
                break;
            t1 = t1.next

                
    def deleteLL(self,value):
        """ 
        # My Code
        prev = self.head
        curr = prev.next
        while(curr != None):
            if(curr.data == value):
                prev.next = curr.next
                break;
            prev = curr
            curr = curr.next """
        t1 = self.head
        prev = t1
        while(t1.next != None):
            if(t1.data == value):
                self.head = t1.next
                break;
            if(t1.data == value):
                prev.next = t1.next
                break;
            else:
                prev = t1
                t1 = t1.next
        if(t1.data == value):
            prev.next = None
                



    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data , end = " ")
            t1 = t1.next
        print(t1.data)
    
obj = SinglyLinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtStart(5)
obj.insertAtMiddle(40,20)
obj.deleteLL(5)
obj.printLL()

# bookmark 40 min( i am not able to understand what should i do.)
