class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic=dict()
        for i in range(len(s)):
            dic[s[i]]=i
        for i in range(len(t)):
            dic[t[i]]=abs(dic[t[i]]-i)
        a=sum(dic.values())
        return a