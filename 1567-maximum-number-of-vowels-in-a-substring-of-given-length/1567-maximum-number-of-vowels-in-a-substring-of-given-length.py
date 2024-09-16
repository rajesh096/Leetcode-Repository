class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        a=['a','e','i','o','u']
        ar=[]
        res=0
        for i in range(k):
            if s[i] in a:
                res+=1
            ar.append(s[i])
        x=res
        for i in range(k,len(s)):
            if s[i-k] in a:
                x-=1
            ar.pop(0)
    
            if s[i] in a:
                x+=1
            ar.append(s[i])
            res=max(res,x)
        return res