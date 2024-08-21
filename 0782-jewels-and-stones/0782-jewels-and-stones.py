class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = {k:v for k,v in (zip(jewels,[0 for i in range(len(jewels))]))}
        for i in stones:
            if i in dic:
                dic[i]+=1
        return sum(dic.values())