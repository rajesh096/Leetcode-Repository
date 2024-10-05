class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p=nums[0]
        if(p<=0) and len(nums)!=1:
            return False
        for i in range(1,len(nums)-1):
            p-=1
            p=max(p,nums[i])
            if(p<=0):
                return False
        return True
