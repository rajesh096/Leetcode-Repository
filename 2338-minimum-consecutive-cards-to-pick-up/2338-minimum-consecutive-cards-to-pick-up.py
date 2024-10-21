class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res=float("inf")
        d={}
        for i in range(len(cards)):
            if cards[i] not in d:
                d[cards[i]]=i
            else:
                res=min(res,i-d[cards[i]]+1)
                d[cards[i]]=i
        if(res!=float("inf")):
            return res
        return -1