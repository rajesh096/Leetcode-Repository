class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=0
        while True:
            z=x^y
            if(z%2==1):
                c+=1
            x>>=1
            y>>=1
            if(z==0):
                break
        return c