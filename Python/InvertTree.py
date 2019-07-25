class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = None

def invertTree(self,root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
