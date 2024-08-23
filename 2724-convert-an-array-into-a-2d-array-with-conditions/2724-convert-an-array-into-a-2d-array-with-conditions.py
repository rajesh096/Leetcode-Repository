class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {k:v for k,v in (zip(nums,[0 for i in range(len(nums))]))}
        for i in nums:
            dic[i]+=1
        res=[[] for i in range(max(dic.values()))]
        for i,j in dic.items():
            for k in range(j):
                res[k].append(i)
        return res