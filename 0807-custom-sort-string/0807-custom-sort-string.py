class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res=""
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in order:
            if i in s:
                res+=i*d[i]
                d[i]=0
        for i,j in d.items():
            if(j>0):
                res+=i*j
        return res