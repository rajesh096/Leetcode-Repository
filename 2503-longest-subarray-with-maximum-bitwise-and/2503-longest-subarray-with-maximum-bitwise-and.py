class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max1=max(nums)
        maxlen=0
        res=0
        for num in nums:
            if num==max1:
                res+=1
            else:
                maxlen=max(maxlen,res)
                res=0
        maxlen=max(maxlen,res)
        return maxlen