class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backt(s,p):
            res.append(p[:])

            for i in range(s,len(nums)):
                p.append(nums[i])
                backt(i+1,p)
                p.pop()
        res=[]
        backt(0,[])
        f=[]
        for i in res:
            if sorted(i) not in f:
                f.append(sorted(i))
        return sorted(f)