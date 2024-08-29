class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        l=set(list(dic.values()))
        if len(l)!=1:
            return False
        else:
            return True