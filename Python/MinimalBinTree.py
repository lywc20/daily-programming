###Naive approach build tree with insertNode()
###Smarter approach is recursively build

class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def createMinimalBST(arr):
    return createMinimalBSTAux(arr,0,len(arr)-1)

def createMinimalBSTAux(arr, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    n = TreeNode(arr[mid])
    n.left = createMinimalBSTAux(arr,start,mid-1)
    n.right = createMinimalBSTAux(arr,mid+1,end)
    return n
