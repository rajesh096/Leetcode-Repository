class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize != 0):
            return False
        maxi = max(hand)
        dic = {}
        hand.sort()
        for i in hand:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for v in dic:
            if(dic[v]!=0):
                val = dic[v]
                for i in range(v,v+groupSize):
                    if(i not in dic):
                        return False
                    if(dic[i]<val):
                        return False
                    dic[i]-=val


        # maxi = max(hand)
        # hl = [0 for i in range(maxi+1)]
        # for i in hand:
        #     hl[i]+=1
        # # print(hl)
        # for i in range(maxi+1):
        #     if(hl[i]>=1):
        #         val = hl[i]
        #         # print(i)
        #         if(i+groupSize-1>maxi):
        #             return False
        #         for i in range(i,i+groupSize):
        #             if(hl[i]==0 or hl[i]<val):
        #                 # print(i)
        #                 return False
        #             hl[i]-=val

        return True