class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        letters=set(s)
        for ch in letters:
            i,j=s.index(ch),s.rindex(ch)
            res=set() 
            for _ in range(i+1,j):
                res.add(s[_])
            ans+=len(res)
        return (ans)