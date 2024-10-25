class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        pre= [1]
        for a, b in pairwise(nums):
            if (a + b) % 2 == 1:
                pre.append(pre[-1] + 1)

            else:
                pre.append(1)
        print(pre)
        res=[]
        for a, b in queries:
            if pre[b] >= b - a + 1:
                res.append(True)
            else:
                res.append(False)
        print(res)
        return res