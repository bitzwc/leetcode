# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
两个单链表相加
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        # 进位
        flag = 0

        # 遍历两个单链表，链表节点的值相加，并把l1 l2的val设置成和
        while l1 is not None and l1 is not None:
            val = l1.val + l2.val
            l1.val = val
            l2.val = val
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is not None:
            # 把l1 l2替换
            l1 = l2

        while l1 is not None:
            val = l1.val + flag
            if val /10 == 1:
                val = val%10
                l1.val = val
                flag = 1
            else:
                flag = 0
            l1 = l1.next

        # 判断最后一个进位是否需要加一个节点
        if flag>0:
            lastNode = ListNode(flag)
            l1.next = lastNode
        return head1
