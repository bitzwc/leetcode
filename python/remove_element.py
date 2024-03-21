def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    while head is not None and head.val == val:
        head = head.next
    p = head
    while p is not None and p.next is not None:
        while p.next is not None and p.next.val == val:
            p.next = p.next.next
        p = p.next
    return head

if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print removeElements(nums,val)