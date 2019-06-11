class RotateK {
    public static void main(String[] args) {
        int n = -4;
        System.out.println(n % 5);
        for (int i : Integer.toString(args)) {
            System.out.println(i);
        }
    }

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }
    public ListNode rotateRight(ListNode head,int n){
        if (head == null || head.next == null) return null;
        ListNode dummy = new ListNode(0);
        ListNode fast = dummy, slow = dummy;
        int length;
        for (length = 0; fast != null; length++) fast = fast.next;
        //get len - n%len th node
        for (int j = length - n % length; j > 0; j--) slow = slow.next;
        fast.next = dummy.next;
        slow.next = null;
        return dummy.next;
    }

}