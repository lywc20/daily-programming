# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if L <= root.val <= R:
            return self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R) + root.val
        elif L > root.val:
            return self.rangeSumBST(root.right,L,R)
        elif R < root.val:
            return self.rangeSumBST(root.left,L,R)


