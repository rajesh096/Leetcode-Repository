class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d={}
        res=[]
        s=s1+" "+s2
        print(s)
        for i in s.split():
            if i not in d:
                d[i]=1
            else:
                d[i]-=1
        for i,j in d.items():
            if(j==1):
                res.append(i)
        return res
        