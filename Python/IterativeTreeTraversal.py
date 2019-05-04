class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root,val):
    node = Node(val)
    tmp = root
    while tmp:
        if val > tmp.val:
            if tmp.right:
                tmp = tmp.right
            else:
                tmp.right = node
                break
        if val < tmp.val:
            if tmp.left:
                tmp = tmp.left
            else:
                tmp.left = node
                break

def Iterative_Prefix(root):
    if not root:
        return []
    result = []
    stack = []
    stack.append(root)
    while stack:
        top = stack[-1]
        result.append(top.val)
        stack.pop()
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)

    print(result)

root = Node(4)
for i in [2,3,6,7]:
    insert(root,i)

Iterative_Prefix(root)
