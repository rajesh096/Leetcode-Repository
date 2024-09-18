from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        nums_str.sort(key=lambda x: x*10, reverse=True)
        largest_num = ''.join(nums_str)
        if largest_num[0] == '0':
            return '0'
        else :
            return largest_num