##Node Class

class Node:

    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.nextNode = nextNode
        #self.min = None

    def get_Val(self):
        return self.data
    
    def get_Next(self):
        return self.nextNode
    
    def set_Next(self,Node):
        self.nextNode = Node

class Stack:

    def __init__(self,top=None):
        self.top = None
        self.minStack = Stack()
    
    def is_Empty(self):
        return self.top == None

    def peek(self):
        return self.top.data

    def push(self,data):
        curr = Node(data)
        if(self.is_Empty()):
            self.top = curr
            #curr.min = curr.data
            self.minStack.push(curr.get_Val())
        else:
            minData = min(curr.get_Val(),self.minStack.peek())
            curr.nextNode = self.top
            self.top = curr
            if self.top.get_Val() <= self.minStack.peek():
                self.minStack.push(minData)
    
    def get_Min(self):
        return self.minStack.peek()
    
    def pop(self):
        if self.is_Empty():
            print('Empty Stack')
        else:    
            val = self.peek()
            self.top = self.top.get_Next()
            if self.minStack.peek() == val:
                self.minStack.top == self.minStack.top.get_Next()
            return val
    
stack = Stack()
for i in range(0,-10,-1):
    stack.push(i)
print(stack.pop())
print(stack.pop())
print(stack.get_Min())

    
    