class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=sorted(nums)
        res=[]
        for i in nums:
            res.append(a.index(i))
        return res
