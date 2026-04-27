#here i am push element from 0th index so accoding to stack my top element is in 0th index.
# STACK using insert method 

# syntax of insert = .insert(index,value)
class stack: 
    def __init__(self):# when we make stack class object then automatically empty list generate
        self.s = []

    def length(self):# joh object banaege wo isme pass ho jayega
        return len(self.s)
    
    #append automatically insert element in last.
    def push(self,value):
        self.s.insert(0,value)# self means talking about the object that you created. and .s to access list.
        #** every time insert in 0th index **
    # list can grow dynamically

    def peek(self): # to see top element in stack
        if (len(self.s) == 0):
            raise Exception("Stack is Empty.")# we have to do exception raise 
        else:
            return self.s[0]
    
    def pop(self): # this is our function
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            return  self.s.pop(0) # to access object and list inside object
        # in case of using append method use only self.s.pop() empty because append insert from last and pop delete form last.

    def printS(self):  
        for i in self.s:
            print(i)

stk = stack()  # here we call stack constructor
stk.push(10)
stk.push(20)
stk.push(30)

print(stk.peek())
print(stk.pop())
print(stk.pop())
print(stk.pop())
# stk.pop()

# my task use append method and use empty pop() method
            


