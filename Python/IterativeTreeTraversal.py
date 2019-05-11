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

## Two queue method
def levelOrderTraversal1(root):
    res = []
    q0 = []
    q1 = []
    q0.append(root)
    while q0 or q1:
        curr = []
        while q0:
            peek = q0.pop(0)
            curr.append(peek.val)
            if peek.left:
                q1.append(peek.left)
            if peek.right:
                q1.append(peek.right)
        res.append(curr)
        q0 = q1
        q1 = []
    for e in res:
        print(e)

## Single queue method with dummy variable
def levelOrderTraversal2(root):
    res = []
    queue = []
    queue.append(root)
    queue.append(None)
    curr = []
    while queue:
       tmp = queue.pop(0)
       if tmp == None:
           res.append(curr)
           curr = []
           if len(queue) > 1:
               queue.append(None)
       else:
           curr.append(tmp.val)
           if tmp.left:
               queue.append(tmp.left)
           if tmp.right:
               queue.append(tmp.right)
    for e in res:
        print(e)

## Maintaining count of each level
def levelOrderTraversal3(root):
    res = []
    queue = []
    curr = []
    currCount = 1
    newCount = 0
    queue.append(root)
    while queue:
        peek = queue.pop(0)
        currCount -= 1
        curr.append(peek.val)
        if peek.left:
            queue.append(peek.left)
            newCount += 1
        if peek.right:
            queue.append(peek.right)
            newCount += 1
        if currCount == 0:
            currCount = newCount
            newCount = 0
            res.append(curr)
            curr = []
    for e in res:
        print(e)

root = Node(2)
for i in [-8,20,-16,-4,10,25,-7,15]:
    insert(root,i)

levelOrderTraversal3(root)
