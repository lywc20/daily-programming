class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.head = None
    
    def traverse(self,head):
        if head:
            print(head.val)
            self.traverse(head.next)
    
    def rotateK(self,key):
    tmp = self.head
    count = 0
    while tmp.next:
        if not tmp.next:
            tail = tmp
        count += 1
        tmp = tmp.next
    tail2id = count - key
    head2id = tail2id + 1
    head2= node(head2.val)
    tmp = head
    while tail2id != 1:
        tmp = tmp.next
        tail2id -= 1
        if tail2id == 2:
            tail2 = tmp.next
    head2 = tail2.next
    while head2:
        list2.append(head2.val)
    while head != tail2id:
        list2.append(head.val)
        head = head.next
    return list2
