class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        result = ""
        for i in range(len(s)):
            temp = ((ord(s[i])-97)+shifts[i])%26
            result +=chr(temp+97)
        return result