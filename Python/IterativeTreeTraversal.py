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
    stack = []
    res = []
    lastNodeVisited = None
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            top = stack[-1]
            if top.right and lastNodeVisited != top.right:
                root = top.right
            else:
                res.append(top.val)
                lastNodeVisited = stack.pop()
    for i in res:
        print(i)

def iterativeInOrder(root):
    result = []
    stack = []
    tmp = root
    while stack or tmp:
        if tmp:
            stack.append(tmp)
            tmp = tmp.left
        else:
            tmp = stack[-1]
            stack.pop()
            result.append(tmp)
            tmp = tmp.right
    for e in result:
        print(e.val)
root = Node(5)
for i in [4,-6,30,-16,2,48,3]:
    insert(root,i)

iterativePostOrder(root)
