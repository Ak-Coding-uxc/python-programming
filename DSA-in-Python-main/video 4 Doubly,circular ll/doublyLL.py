class Node:
    def __init__(self , value , next = None,prev = None):
        self.data = value
        self.next = next
        self.prev = prev

class SinglyLL:
    def __init__(self , head = None):
        self.head = head

    def insertAtStart(self,value):
        temp = Node(value)
        t1 = self.head
        if(t1 != None):
           t1.prev = temp
           temp.next = t1
           self.head = temp
        else:
            self.head = temp # head object ka variable hota hai (instance variable). means class ka varible
# ye variable puri class ke liye available hai

    def insertAtEnd(self,value):# self is jis object ki baat ho rhi h
        temp = Node(value)
        t1 = self.head
        if(t1 != None):
            while(t1.next != None):
               t1 = t1.next
            t1.next = temp
            temp.prev = t1
        else:
            self.head = temp

    def insertAtMiddle(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
        else: 
            prev = self.head
            n = int(input("Insert after which value: "))
            while(prev != None):
                if(prev.data == n):
                    t1 = prev.next
                    temp.prev = prev
                    temp.next = t1
                    prev.next = temp
                    t1.prev = temp
                    break;
                else:
                    prev = prev.next


    
    def deleteFromStart(self):
        t1 = self.head
        if(t1 == None):
            print("The List is Empty")
        else: 
            self.head = t1.next

    def deleteFromEnd(self):
        if(self.head == None):
            print("Please make list first")
        else:
            t1 = self.head
            curr = t1.next
            while(curr.next != None):
                t1 = curr
                curr = curr.next
            t1.next = curr.next

    def deleteFromMiddle(self):
        if(self.head == None):
            print("Please I request you please make list first.")
        else:
            n = int(input("Term after you want to delete: "))
            k = 1
            prev = self.head
            curr = prev.next
            while(k != n):
                k = k + 1
                prev = curr
                curr = curr.next
            t1 = curr.next
            prev.next = t1
            t1.prev = prev

    def deleteLL(self):
        if(self.head != None):
            temp = self.head
            curr = temp.next
            n = int(input("Enter value you want to delete: "))
            if(temp.data == n):
                self.head = curr
                return
            while(temp != None):
                if(curr.data == n):
                    temp.next = curr.next
                    return
                else:
                    temp = curr
                    curr = curr.next

    def printf(self):
        if(self.head == None):
            print("This is empty list")
        else:
            temp = self.head
            while(temp.next != None):
                print(temp.data , end = " <--> ")
                temp = temp.next
            print(temp.data)

obj = SinglyLL()

obj.insertAtStart(100)
obj.insertAtStart(90)
obj.printf()

obj.insertAtEnd(101)
obj.printf()

obj.insertAtStart(1)
obj.printf()

obj.deleteLL()
obj.printf()
# obj.deleteFromStart()
# obj.printf()

# obj.deleteFromEnd()
# obj.printf()



