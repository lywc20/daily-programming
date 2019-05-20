# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node.next:
            return
        else:
            curr = node
            while curr:
                if curr.next and curr.next.next:
                    curr.val = curr.next.val
                    curr = curr.next
                elif curr.next and not curr.next.next:
                    curr.val = curr.next.val
                    curr.next = None
                    break
