class Solution:
    def minimumSteps(self, s: str) -> int:
        if(len(s)==1):
            return 0
        i,j=0,len(s)-1
        res=0
        ar=list(s)
        while i<j:
            if(ar[i]=='1' and ar[j]=='0'):
                ar[i],ar[j]=ar[j],ar[i]
                res+=j-i
                i+=1
                j-=1
            else:
                if(ar[j]=='1'):
                    j-=1
                if(ar[i]=='0'):
                    i+=1
        return res