###Designing Stack with O(1) min,pop,push
class Node(obj):
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
        self.min = None
    
    def get_val(self):
        return self.data

    def get_next(self):
        return self.next_node
    
    def set_next(self)

class Stack(obj):
    def __init__(self,top=None):
        self.top = top
        self.min = None
    
    def push(self,node):
        if self.top == None:
            self.top = node
            self.top.min = self.top.get_val()
        else:
            if node.get_val() > self.top.min:
                node.min = self.top.min
            else:
                node.min = node.get_val
            node.next_node = self.top()
            self.top = node
