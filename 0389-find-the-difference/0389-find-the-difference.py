class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in s:
            d[i]-=1
        for i,j in d.items():
            if(j==1):
                return i
        return 0