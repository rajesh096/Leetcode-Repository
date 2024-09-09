class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c=0
        for i in s:
            c=c^(ord(i))
        for i in t:
            c=ord(i)^c
        return chr(c)