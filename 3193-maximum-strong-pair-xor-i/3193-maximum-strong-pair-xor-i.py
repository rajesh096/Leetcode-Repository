class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        mini=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    n=nums[i]^nums[j]
                    mini=max(mini,n)
        return mini