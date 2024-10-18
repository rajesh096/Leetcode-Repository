from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res=[]
        d=defaultdict(list)
        for i in range(1,len(nums)+1):
            res.extend(combinations(nums,i))
        a= [list(i) for i in res]
        # print(a)
        arr=[]
        for i in range(len(a)):
            l=0
            for j in range(len(a[i])):
                l|=a[i][j]
            arr.append(l)
        # print(max(arr))
        # print(arr.count(max(arr)))
        return arr.count(max(arr))