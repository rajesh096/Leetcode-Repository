class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i,j in dic.items():
            if j>=2:
                return i