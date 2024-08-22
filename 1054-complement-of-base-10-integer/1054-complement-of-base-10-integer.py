class Solution:
    def bitwiseComplement(self, num: int) -> int:
        s=bin(num)
        s=s[2:]
        s=list(s)
        print(s)
        for i in range(len(s)):
            if s[i]=='0':
                s[i]='1'
            else:
                s[i]='0'
        res="".join(s)
        return int(res,2)