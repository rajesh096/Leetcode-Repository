class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        c=0
        res=0
        for i in range(len(s)-1): 
            if(ord(s[i])+1==ord(s[i+1])):
                c+=1
            else:
                c+=1
                res=max(res,c)
                c=0
        c+=1
        
        res=max(res,c)
        return res