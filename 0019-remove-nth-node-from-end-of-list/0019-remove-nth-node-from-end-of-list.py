# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        prev=None
        l=0
        while(p):
            l+=1
            p=p.next
        l=l-n+1
        p=head
        x=0
        while(p):
            x+=1
            if(x==l):
                if(prev==None):
                    head=p.next
                    prev=p
                    p=p.next
                else:
                    prev.next=p.next
                    p=p.next
            else:
                prev=p
                p=p.next

        return head