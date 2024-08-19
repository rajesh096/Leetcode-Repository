class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dis = dict()
        for i in set(nums):
            dis[i]=0
        for i in nums:
            dis[i]+=1
        for i,j in dis.items():
            if dis[i]==1:
                return i
        return 0