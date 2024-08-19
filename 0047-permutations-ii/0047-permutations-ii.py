class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums[:]) 
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  
                backtrack(start + 1)  
                nums[start], nums[i] = nums[i], nums[start]  

        backtrack(0)
        f=[]
        for i in result:
            if i not in f:
                f.append(i)
        return sorted(f)