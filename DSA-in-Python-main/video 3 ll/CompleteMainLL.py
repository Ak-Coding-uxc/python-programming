class Node:
    def __init__(self , value , next = None):
        self.data = value
        self.next = next

class SinglyLL:
    def __init__(self , head = None):
        self.head = head

    def insertAtStart(self,value):
        temp = Node(value)
        if(self.head != None):
            temp.next = self.head
            self.head = temp
        else:
            self.head = temp # head object ka variable hota hai (instance variable). means class ka varible
# ye variable puri class ke liye available hai

    def insertAtEnd(self,value):# self is jis object ki baat ho rhi h
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
               t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtMiddle(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
        else: 
            t1 = self.head
            # n = int(input("Insert after which term: "))
            n = 2
            k = 1
            while(k != n):
                k = k + 1
                t1 = t1.next
            temp.next = t1.next
            t1.next = temp
    
    def deleteFromStart(self):
        if(self.head == None):
            print("The List is Empty")
        else:
            self.head = self.head.next

    def deleteFromEnd(self):
        if(self.head == None):
            print("Please make list first")
        else:
            prev = self.head
            curr = prev.next
            while(curr.next != None):
                prev = curr
                curr = curr.next
            prev.next = curr.next

    def deleteFromMiddle(self):
        if(self.head == None):
            print("Please I request you please make list first.")
        else:
            n = int(input("Term after you want to delete: "))
            k = 1
            if(n < k):
                print("Please Enter current term")
            else:
                prev = self.head
                curr = prev.next
                while(k != n):
                    k = k + 1
                    prev = curr
                    curr = curr.next
                prev.next = curr.next

    def printf(self):
        if(self.head == None):
            print("This is empty list")
        else:
            temp = self.head
            while(temp.next != None):
                print(temp.data , end = " , ")
                temp = temp.next
            print(temp.data)

obj = SinglyLL()
# obj.insertAtStart(int(input("Enter your value: ")))
obj.insertAtStart(40)
obj.insertAtStart(50)
obj.insertAtStart(60)
obj.insertAtStart(70)
obj.insertAtEnd(20)

obj.insertAtMiddle(1000)

obj.printf()

obj.deleteFromStart()

obj.printf()

obj.deleteFromEnd()

obj.printf()

obj.deleteFromMiddle()

obj.printf()