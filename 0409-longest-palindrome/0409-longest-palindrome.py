class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic={k:v for k,v in zip(s,[0 for _ in range(len(s))])}
        for i in s:
            dic[i]+=1
        dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        res=0
        f=True
        for i,j in dic.items():
            if(j%2==1):
                res+=j-1
                f=False
            else:
                res+=j
        if f==False:
            res+=1
        return res
        