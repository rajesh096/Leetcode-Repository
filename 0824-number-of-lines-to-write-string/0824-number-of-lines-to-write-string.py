class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count=0
        c=1
        for i in s:
            ch = ord(i)-97
            count+=widths[ch]
            if count>100:
                c+=1
                count=widths[ch]

        return [c,count]