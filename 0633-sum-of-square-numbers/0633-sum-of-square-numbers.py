class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=int(c**0.5)
        j=0
        sum=0
        while(j<=i):
            sum+=((i*i)+(j*j))
            if(sum==c):
                return True
            if(sum>c):
                i-=1
            else:
                j+=1
            sum=0
        return False        