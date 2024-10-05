# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        n=0
        p=head
        while(p):
            arr.append(p.val)
            n+=1
            p=p.next
        res=[0]*n
        st=[]
        for i in range(n):
            while st and arr[st[-1]]<arr[i]:
                res[st.pop()]=arr[i]
            st.append(i)
        return res