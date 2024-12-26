class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        p=[1]*len(nums)
        for i in range(len(nums)):
            p[(i-nums[i]+1)%len(nums)]-=1
        for i in range(1,len(nums)):
            p[i]+=p[i-1]
        return p.index(max(p))