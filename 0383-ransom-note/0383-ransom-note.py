class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        d1={}
        for i in magazine:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in ransomNote:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in ransomNote:
            if(i not in d) or d[i]<d1[i]:
                return False
        return True