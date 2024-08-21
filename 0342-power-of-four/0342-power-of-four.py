class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n>0):
            return ((n&n-1==0) & (n%3==1))
        else:
            return False