def isPalinedrome(self,head):
    f = s = head
    while f and f.next:
        f = f.next.next
        s = s.next
    if f:
        s = s.next
    s = reverseLL(s)
    f = head
    while s:
        if s.val != f.val:
            return False
        s = s.next
        f = f.next
    return True

def reverseLL(self, head):
    p = None
    while head:
        n = head.next
        head.next = p
        p = head
        head = n
    return p
