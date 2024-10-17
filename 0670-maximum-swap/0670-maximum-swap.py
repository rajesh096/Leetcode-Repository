class Solution:
    def maximumSwap(self, num: int) -> int:
        num=str(num)
        res=[]
        for i in num:
            res.append(int(i))
        for i in range(len(res)-1):
            if res[i]<max(res[i+1:]):
                m=max(res[i+1:])
                for k in range(i+1,len(res)):
                    if m==res[k]:
                        j=k
                res[i],res[j]=res[j],res[i]
                break
        s=""
        for i in res:
            s+=str(i)
        return int(s)
        