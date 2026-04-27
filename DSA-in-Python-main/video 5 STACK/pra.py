class Stack:
    def __init__(self):
        self.s = []
    
    def push(self , value):
        self.s.append(value)
    
    def pop(self):
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            return self.s.pop()
        
    def peek(self):
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            k = len(self.s) - 1
            return self.s[k]
    
    def pri(self):
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            for x in self.s:
                print(x , end = " , ")
            print()

obj = Stack()
obj.push(99)
obj.push(45)
obj.push(63)
obj.push(105)
obj.pri()

print(obj.pop())
obj.push(99)
obj.push(45)
obj.push(63)
obj.pri()     
print(obj.peek())      