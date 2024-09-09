class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1:
            return 0
        c=0
        x=n
        while(x>1):
            if x%2==0:
                x>>=1
            else:
                if x==3 or x&3==1:
                    x-=1
                else:    
                    x+=1
            c+=1
            # x>>=1
        return c
        