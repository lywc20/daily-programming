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

def iterativePreOrder(root):
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

def iterativePostOrder(root):
    if not root:
        return []
    result = []
    stack = []
    stack.append(root)
    while stack:
        tmp = stack[-1]
        if tmp.left and tmp.left.val not in result:
            stack.append(tmp.left)
        else:
            stack.pop()
            result.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
    print(result)

root = Node(5)
for i in [3,1,0,2,8,6,10,11]:
    insert(root,i)

iterativePostOrder(root)
