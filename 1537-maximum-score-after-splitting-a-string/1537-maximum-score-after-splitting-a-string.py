class Solution:
    def maxScore(self, s: str) -> int:
        tot_O = 0
        for i in s:
            if(i=="0"):
                continue
            else:
                tot_O+=1
        lef_ss = 1 if s[0]=="0" else 0
        rgt_ss = tot_O-1 if s[0]=="1" else tot_O
        maxi=lef_ss + rgt_ss
        for i in range(1,len(s)-1):
            if(s[i]=="0"):
                lef_ss +=1
            else:
                rgt_ss-=1
            maxi = max(maxi,lef_ss+rgt_ss)
        return maxi