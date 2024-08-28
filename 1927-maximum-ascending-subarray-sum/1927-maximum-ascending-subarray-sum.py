class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi=0
        s=0
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):
                s+=nums[i]
            else:
                s+=nums[i]
                maxi=max(s,maxi)
                s=0
        s+=nums[-1]
        maxi=max(s,maxi)
        return maxi