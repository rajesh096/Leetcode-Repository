class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)
        subsets=1<<n
        res=[]
        for num in range(subsets):
            bor=0
            for i in range(n):
                if num&(1<<i):
                    bor|=nums[i]
            res.append(bor)
        m=max(res)
        return res.count(m)