class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = None

    def insert(self,root,val):
        node = Node(val)
        curr = root
        while curr:
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

    def isSym(self,root):
        return root == None or auxIsSym(root.left,root.right)
    
    def auxIsSym(self,root1,root2):
        if root1 == None || root2 == None:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return auxIsSym(root1.left,root2.right) and auxIsSym(root1.right,root2.left)
