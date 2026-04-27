class Node:# why => To create Node
    def __init__(self,value, next = None):
        self.data = value
        self.next = next
    
class CircularLL: #why to insert,delete or print operation of list
    def __init__(self, head = None):
        self.head = head
        # self.tail = head
    
    def startInsert(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            self.head.next = self.head
        else:
            temp.next = self.head
            tail = self.head
            while(tail.next != self.head):
                tail = tail.next
            tail.next = temp
            self.head = temp

    def middleInsert(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            self.head.next = self.head
        else:
            n = int(input("Insert in which index: "))
            curr = self.head
            prev = curr
            k = 1
            if(n == 1):
                tail = self.head
                while(tail.next != self.head):
                    tail = tail.next
                tail.next = temp
                temp.next = self.head
                self.head = temp
                return
            while(k != n):
                prev = curr
                curr = curr.next
                k = k + 1
                if(prev.next == self.head):
                    print("out of bound")
                    return
            temp.next = prev.next
            prev.next = temp

    def endInsert(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            self.head.next = self.head
        else:
            tail = self.head
            while(tail.next != self.head):
                tail = tail.next
            tail.next = temp
            temp.next = self.head  

    def deleteLL(self):
        k = int(input("Enter value you want to delete: "))
        prev = self.head
        curr = prev
        if(prev.data == k):
            tail = self.head
            while(tail.next != self.head):
                tail = tail.next
            self.head = prev.next
            tail.next = self.head
            return
        else:    
            while(prev.next != self.head):
                if(curr.data != k):
                    prev = curr
                    curr = curr.next
                else:
                    prev.next = curr.next
                    return
            print("Value not found")

    def printLL(self):
        print("Printing values: ")
        if(self.head == None):
            print("List is Empty")
        else:
            t = self.head
            while(t.next != self.head):
                print(t.data , end = " --> ")
                t = t.next
            print(t.data)
    
    def value(self):# “Jab hum class ke andar object ke function ko define karte hain tab self likhna padta hai.”
        i = int(input("Enter value: "))
        return i
# video to see ( stack and python oop from code with harray.)

obj = CircularLL()
print("Insert in Beginning")
obj.startInsert(obj.value())
obj.startInsert(obj.value())
obj.startInsert(obj.value())
obj.printLL()

print("Insert in Middle")
obj.middleInsert(obj.value())
obj.printLL()

print("Insert in End")
obj.endInsert(obj.value())
obj.printLL()

print("Delete value from Linked List")
obj.deleteLL()
obj.printLL()



