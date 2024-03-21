class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        k = head
        p = l1
        q = l2
        while p is not None and q is not None:
            if p.val<=q.val:
                k.next = p
                p = p.next
            else:
                k.next = q
                q = q.next
            k = k.next
        k.next = p or q
        return head.next