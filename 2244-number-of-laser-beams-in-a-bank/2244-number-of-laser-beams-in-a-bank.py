class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 1
        f = -1
        for i in bank:
            p = i.count('1')
            if(p!=0):
                if(f!=-1):
                    res+=(prev*p)
                prev = p
                f=1
        return res
