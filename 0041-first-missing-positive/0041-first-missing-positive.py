class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=set(nums)
        x=1
        while True:
            if x not in a:
                return x
            else:
                x+=1