class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        for i in arr:
            n=abs(i-x)
            res.append(n)
        re1=sorted(res)
        print(res)
        r=[]
        for i in range(k):
            n=res.index(re1[i])
            res[n]=-1
            r.append(arr[n])
        
        return sorted(r)