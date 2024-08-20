class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        for i in range(len(nums)):
            result+=accumulate(nums[i:])
        result = sorted(result)
        return sum(result[left-1:right]) % (10 ** 9 + 7)