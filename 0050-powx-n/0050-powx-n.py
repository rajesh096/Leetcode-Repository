class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            n= abs(n)
            x=1/x
        def func(x, n):
            if n == 0:
                return 1
            half = func(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        return func(x,n)