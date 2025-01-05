class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pres = [0]*n
        for i in shifts:
            if(i[2]==0):
                pres[i[0]]-=1
                if(i[1] != n-1):
                    pres[i[1]+1]+=1 
            else:
                pres[i[0]]+=1
                if(i[1] != n-1):
                    pres[i[1]+1]-=1
        for i in range(1,n):
            pres[i]+=pres[i-1]
        res = ""
        for i in range(n):
            val = (ord(s[i])-97)+pres[i]
            if(val>=26):
                val%=26
                
            elif(val<0):
                val=26-((abs(val)%26))
                val%=26
            res+=chr(97+val)
        return res
