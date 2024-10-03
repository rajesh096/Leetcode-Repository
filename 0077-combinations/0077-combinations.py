class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        def cmbn(s,ar):
            if(len(ar)==k):
                res.append(ar[:])
            
            for i in range(s,len(nums)):
                ar.append(nums[i])
                cmbn(i+1,ar)
                ar.pop()
        res=[]
        cmbn(0,[])
        return res