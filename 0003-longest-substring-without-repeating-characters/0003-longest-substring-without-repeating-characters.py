class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=[]
        i,j=0,0
        st=""
        if s==" ":
            return len(s)
        if len(s)==1:
            return 1
        maxi=0
        while(i<len(s)):
            
            if s[j] not in st:
                st=s[i:j+1]
                j+=1
            else:
                res.append(st)
                maxi=max(maxi,len(st))
                st=""
                i+=1
                j=i
            
            if j==len(s):
                i+=1
                j=i
        print(len(s))
        return maxi

