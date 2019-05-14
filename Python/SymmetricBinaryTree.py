class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = None

    def insert(self,root,val):
        node = Node(val)
        curr = root
        while curr:
            if val > curr.val:
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

    def isSym(self,root):
        return root == None or self.auxIsSym(root.left,root.right)
    
    def auxIsSym(self,root1,root2):
        if root1 == None or root2 == None:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return self.auxIsSym(root1.left,root2.right) and self.auxIsSym(root1.right,root2.left)

    def iterativeIsSym(self,root: Node) -> bool:
        if root == None:
            return True
        
        leftStack = []
        rightStack = []
        leftStack.append(root)
        rightStack.append(root)

        while leftStack and rightStack:
            leftChild = leftStack.pop()
            rightChild = rightStack.pop()

            if leftChild.val != rightChild.val:
                return False
            
            if leftChild.left == None or rightChild.right == None:
                if leftChild.left != rightChild.right:
                    return False
                else:
                    leftStack.append(leftChild.left)
                    rightStack.append(rightChild.right)
            if leftChild.right == None or rightChild.left == None:
                if leftChild.right != rightChild.left:
                    return False
                else:
                    leftStack.append(leftChild.right)
                    rightStack.append(rightChild.left)
        return True
                

