class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        maxi=prices[0]
        res=0
        for i in range(1,len(prices)):
            if(prices[i]<maxi):
                res+=(maxi-minp)
                minp=prices[i]
                maxi=prices[i]
            elif(maxi<prices[i]):
                maxi=prices[i]
                
        res+=(maxi-minp)
        return res