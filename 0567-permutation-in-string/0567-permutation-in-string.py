class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1=sorted(s1)
        n=len(s1)
        res=""
        for i in range(n):
            res+=s2[i]
        if s1==sorted(res):
            return True
        for i in range(len(s2)-n):
            res=res[1:]
            res+=s2[n+i]
            if(s1==sorted(res)):
                return True
        return False