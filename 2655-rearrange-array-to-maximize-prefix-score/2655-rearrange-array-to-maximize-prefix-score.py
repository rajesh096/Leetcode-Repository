class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        j=0
        count=0
        for i in range(len(nums)):
            j+=nums[i]
            if j>0:
                count+=1
        return count