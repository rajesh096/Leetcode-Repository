class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st=""
        for i in s:
            a=ord(i) - 96
            st+=str(a)
        res=0
        for i in range(k):
            x=0
            for j in st:
                x+=int(j)
            st=str(x)
            res=x
        return res
        