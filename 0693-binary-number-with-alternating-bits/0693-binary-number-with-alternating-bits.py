class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=n&1
        n>>=1
        while(n>0):
            a=n&1
            if(a==x):
                return False
            x=a
            n>>=1
        return True