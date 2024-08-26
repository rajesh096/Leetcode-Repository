class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        for i,j in dic.items():
            if j>=2:
                res.append(i)
        return res