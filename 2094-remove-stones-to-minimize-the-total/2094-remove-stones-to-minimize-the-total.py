import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        res=0
        m=[-n for n in piles]
        heapq.heapify(m)
        for i in range(k):
            maxi=-heapq.heappop(m)
            heapq.heappush(m,-(maxi-floor(maxi/2)))
        for i in m:
            res+=abs(i)
        return res