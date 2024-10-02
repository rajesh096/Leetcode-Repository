class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(arr)
        d = {}
        c = 1
        for i in range (len(arr)):
            if a[i] not in d:
                d[a[i]] = c
                c+=1
            # print(d)
        l = []
        for i in arr:
            l.append(d[i])
        return l