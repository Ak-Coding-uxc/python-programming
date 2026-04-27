class Node:
    def __init__(self,value,next = None,prev = None):
        self.data = value
        self.prev = prev
        self.next = next

class DoublyCircularLL:
    def __init__(self,head = None):
        self.head = head # because to show this is empty list
    
    def insertStart(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            self.head.next = self.head
            self.head.prev = self.head
        else:
            temp.next = self.head
            t1 = self.head
            while(t1.next != self.head):
                t1 = t1.next
            t1.next = temp
            temp.prev = t1
            self.head = temp
    
    def insertMiddle(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            temp.next = self.head
            temp.prev = self.head
        else:
            n = int(input("Where to insert: "))
            k = 1
            prev = self.head
            curr = prev
            if(n == 1):
                while(prev.next != self.head):
                    prev = prev.next
                temp.next = self.head
                prev.next = temp
                temp.prev = prev
                self.head.prev = temp
                self.head = temp
                return
            else:
                while(k != n):
                    if(prev.next == self.head):
                        print("Out of bound")
                        return
                    prev = curr
                    curr = curr.next
                    k = k + 1
                temp.next = curr
                temp.prev = prev
                prev.next = temp
                curr.prev = temp
    
    def insertEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            temp.next = temp
            temp.prev = temp
            self.head = temp
        else:
            t1 = self.head
            while(t1.next != self.head):
                t1 = t1.next
            t1.next = temp
            temp.prev = t1
            temp.next = self.head
            self.head.prev = temp

    def deleteLL(self):
        if(self.head == None):
            print("Linked List not found")
        else:
            n = int(input("Enter value you want to delete: "))
            prev = self.head
            curr = prev
            if(prev.data == n):
                temp = self.head
                while(temp.next != self.head):
                    temp = temp.next
                prev = prev.next
                prev.prev = temp
                temp.next = prev
                self.head = prev
                return
            while(prev.next != self.head):
                if(curr.data == n):
                    prev.next = curr.next
                    t1 = curr.next
                    t1.prev = prev
                    return
                else:
                    prev = curr
                    curr = curr.next
            print(f"Value {n} is not found in the list")

            

    def printLL(self):
        if(self.head == None):
            pritn("List not found")
        else:
            t1 = self.head
            while(t1.next != self.head):
                print(t1.data , end = "<-->")
                t1 = t1.next
            print(t1.data)

obj = DoublyCircularLL()
obj.insertStart(12)
obj.insertStart(23)
obj.insertStart(56)
obj.printLL()


obj.insertEnd(33)
obj.insertEnd(64)
obj.insertEnd(99)
obj.printLL()

# obj.insertMiddle(88)
# obj.printLL()
# obj.insertMiddle(63)
# obj.printLL()
# obj.insertMiddle(1990)
# obj.printLL()

obj.deleteLL()
obj.printLL()


            

        
    
    