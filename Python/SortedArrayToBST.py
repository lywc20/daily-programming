# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    
       def dfs(L,R):
           mid = (L+R)//2
           root = TreeNode(nums[mid])
           root.left = dfs(root.left,0,mid)
           root.right = dfs(root.right,mid+1,R)
           return root
       return dfs(0,len(nums)

