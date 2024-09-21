# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        a=[]
        while p:
            a.append(p.val)
            p=p.next
        res=[]
        sum=0
        for i in a:
            if(i==0):
                if(sum!=0):
                    res.append(sum)
                sum=0
            else:
                sum+=i
        p=head
        for i in range(len(res)):
            p.val=res[i]
            if(i==len(res)-1):
                p.next=None
            p=p.next
        return head