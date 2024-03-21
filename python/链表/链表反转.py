class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def reverseList(head):
    if head.next==None:
        return None
    tmp=head.next
    while tmp.next!=None:
        p=tmp.next
        tmp.next=p.next
        p.next=head.next
        head.next=p
    return head

head=ListNode(None)
l1=ListNode(2)
head.next=l1
l2=ListNode(1)
l1.next=l2
l3=ListNode(4)
l2.next=l3
result=[]
h=reverseList(head)
while h!=None:
    result.append(h.val)
    h=h.next
print(result[1:])

