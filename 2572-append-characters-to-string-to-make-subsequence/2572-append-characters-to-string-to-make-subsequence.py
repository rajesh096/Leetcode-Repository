class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        for i in s:
            if(i==t[j]):
                j+=1
                if(j>=len(t)):
                    break
        return len(t)-j