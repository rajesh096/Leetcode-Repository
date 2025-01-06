class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        bonce = 0
        aonce = 0
        total = 0
        res = []
        if(boxes[0]=='0'):
            for i in range(len(boxes)):
                if(boxes[i]=='1'):
                    aonce += 1
                    total += i
        else:
            for i in range(len(boxes)):
                if(boxes[i]=='1'):
                    aonce += 1
                    total += i+1
        for i in range(len(boxes)):
            if(boxes[i]=='1'):
                total -= 1
                if(aonce>0):
                    aonce -= 1
                total -= aonce
                total += bonce
                bonce += 1
                res.append(total)
            else:
                if i!=0:
                    total -= aonce
                    total += bonce
                res.append(total)
                
        return res
        