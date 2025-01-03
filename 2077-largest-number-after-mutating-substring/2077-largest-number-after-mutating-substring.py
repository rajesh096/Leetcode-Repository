class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res = ""
        f1 = True
        f2 = True
        f3 = True
        for i in range(len(num)):
            if(f1==False and f2==False):
                res+=num[i]

            else:
                temp = int(num[i])
                if(temp <= change[temp]):
                    res += str(change[temp])
                    
                    if(temp == change[temp]):
                        f3=False
                    else:
                        f1=False
                else:
                    res+=num[i]
                    if(f1==False):
                        f2=False
        return res