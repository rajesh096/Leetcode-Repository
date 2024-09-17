class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        if(len(nums)%2==0):
            mid-=1
        res=0
        for i in nums:
            res+=(abs(i-nums[mid]))
        return res