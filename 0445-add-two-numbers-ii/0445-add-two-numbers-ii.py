# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a1=""
        a2=""
        p=l1
        while(p):
            a1=a1+str(p.val)
            p=p.next
        p=l2
        while(p):
            a2=a2+str(p.val)
            p=p.next
     
        s=str(int(a1)+int(a2))
        p=l1
        l=0
        for i in s:
            l+=1
            p.val=int(i)
            if(p.next==None and l<len(s)):
                p.next=ListNode(i)
            p=p.next
        return l1