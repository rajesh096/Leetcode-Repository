class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre_sum = 0
        for i in nums:
            pre_sum+=i
        result = 0
        local_sum = 0
        for i in range(len(nums)-1):
            local_sum+=nums[i]
            if(pre_sum-local_sum <= local_sum):
                result +=1
        return result