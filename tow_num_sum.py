# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        # 进位
        flag = 0

        # 遍历两个单链表，链表节点的值相加，并把l1 l2的val设置成和
        while l1 is not None and l1 is not None:
            val = l1.val + l2.val
            l1.val = val
            l2.val = val
            p1 = l1
            p2 = l2
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is not None:
            # 把l1 l2替换
            temp = l1
            l1 = l2
            l2 = temp

        while l1 is not None:
            val = l1.val + flag
            if val>9:
                val = val - 10
                flag = 1
            p1 = l1
            l1 = l1.next

        # 判断最后一个进位是否需要加一个节点
        if flag>0:
            p2 = ListNode()
            p2.val = flag
            p2.next = None
            p1.next = p2
        return head1

    def input_data(self, nums):
        for i in range(len(nums)):
            if i == 0:
                head = ListNode
                head.val = nums[i]
                head.next =
            else:

        node3 = ListNode
        node3.val = 3
        node3.next = None

        node2 = ListNode
        node2.val = 4
        node2.next = node3

        node1 = ListNode
        node1.val = 2
        node1.next = node2
        print node1
