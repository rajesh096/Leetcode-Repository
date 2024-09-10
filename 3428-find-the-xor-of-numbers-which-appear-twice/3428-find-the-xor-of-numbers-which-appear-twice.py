class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]^nums[j]==0):
                    res=res^nums[i]
        return res