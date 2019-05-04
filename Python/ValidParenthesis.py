class Node:
    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.nextNode = nextNode
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.nextNode

class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top == None
    
    def push(self,data):
        node = Node(data)
        if(self.is_empty()):
            self.top = node
        else:
            node.nextNode = self.top
            self.top = node
    
    def peek(self):
        if(self.is_empty()):
            print("Stack is Empty\n")
        else:
            return self.top.get_data()
        
    def pop(self):
        if self.is_empty():
            print("Stack is Empty\n")
            return
        else:
            val = self.top.get_data()
            self.top = self.top.get_next()
            return val
    
    def print_Stack(self):
        if self.is_empty():
            print("Empty Stack")
        else:
            curr = self.top
            while(curr != None):
                print(curr.get_data())
                curr = curr.get_next()

# ()  {}  []
def validate(inp):
    if len(inp) <= 0:
        return False
    stack = Stack()
    for i in inp:
        if i in ['[','{','(']:
            stack.push(i)
        elif i == '}':
            if stack.pop() != '{':
                return False
        elif i == ']':
            if stack.pop() != '[':
                return False
        elif i == ')':
            if stack.pop() != '(':
                return False
    return stack.is_empty()

t1 = '[]'
t2 = '[]'
t3 = '(}'
print(validate(t2))
