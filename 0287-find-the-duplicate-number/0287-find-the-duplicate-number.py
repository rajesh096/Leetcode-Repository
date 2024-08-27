class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        for i,j in dic.items():
            if j>=2:
                return i