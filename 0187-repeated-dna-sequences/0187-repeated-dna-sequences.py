class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d={}
        if(len(s)<10):
            return []
        for i in range(len(s)):
            if(s[i+0:10+i] not in d):
                d[s[i+0:10+i]] = 1
            else:
                d[s[i+0:10+i]]+=1
        res=[]
        for i,j in d.items():
            if(j>1):
                res.append(i)
        return res