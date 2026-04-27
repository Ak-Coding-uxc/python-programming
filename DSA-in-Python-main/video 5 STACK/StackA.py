# Stack using append method
class Stack:
    def __init__(self):
        self.s = []
    
    def push(self,value):
        self.s.append(value) # insert in last
    
    def pop(self):
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
          return self.s.pop() # last value delete
        
    def peek(self):
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            k = len(self.s) - 1
            return self.s[k]
    
    def printS(self):
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            for i in self.s:
                print(i , end = " ")
            print()
"""
    raise Exception ka matlab kya hai?
👉 Program ko bolna: “Yahan kuch galat ho gaya, aage mat chalo”
 this throw an error when invalid condition occur.
 """ 

stk = Stack() # new stack object is created
stk.push(20)
stk.push(10)
stk.push(40)
stk.push(50)
stk.printS()
print(stk.pop())
print(stk.pop())
stk.printS()
print(stk.peek())
