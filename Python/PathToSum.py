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
    def pathToSum(self,root : Node, s : int) -> bool:
        if not root:
            return False
        if root.val == s and not root.left and not root.right:
            return True
        return self.pathToSum(root.left,s - root.val) or self.pathToSum(root.right,s-root.val)


