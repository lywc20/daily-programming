"""
Given the list of nodes in posterOrder/preOrder and inOrder
create a tree from the lists
"""
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def buildTree(postOrder:[int],inOrder:[int]):
    if not postOrder or not inOrder:
        return None
    root = Node(postOrder.pop())
    rootIndex = inOrder.index(root.val)
    root.right = buildTree(postOrder,inOrder[rootIndex+1:])
    root.left = buildTree(postOrder,inOrder[:rootIndex])
    return root

def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.val)
    inOrderTraversal(root.right)

postOrder = [9,3,15,20,7]
inOrder = [9,15,7,20,3]

root = buildTree(postOrder,inOrder)
inOrderTraversal(root)