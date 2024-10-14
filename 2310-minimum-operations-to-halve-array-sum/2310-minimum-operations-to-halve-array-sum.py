class Solution:
    def halveArray(self, nums: List[int]) -> int:
        res=0
        m=[-n for n in nums]
        heapq.heapify(m)
        x=sum(nums)
        n=x
        half=x/2
        while True:
            maxi=-heapq.heappop(m)
            x-=(maxi-(maxi/2))
            res+=1
            if((n-x)>=half):
                break
            heapq.heappush(m,-(maxi/2))
        return res