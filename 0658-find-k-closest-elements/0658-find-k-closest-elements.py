class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        for i in arr:
            n=abs(i-x)
            res.append(n)
        re1=sorted(res)
        print(res)
        r=[]
        for i in re1[:k]:
            n=res.index(i)
            res[n]=-1
            r.append(arr[n])
        # dic=dict(sorted(dic.items(), key=lambda item: item[1]))
        # for i,j in dic.items():
        #     if k!=0:
        #         res.append(i)
        #         k-=1
        #     else:
        #         break
        
        return sorted(r)