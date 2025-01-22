class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1 = target[0]
        t2 = target[1]
        t3 = target[2]
        temp = []
        for i in triplets:
            if(i[0]>t1 or i[1]>t2 or i[2]>t3):
                continue
            else:
                temp.append(i)
        m1,m2,m3 = 0,0,0
        for t in temp:
            m1 = max(t[0],m1)
            m2 = max(t[1],m2)
            m3 = max(t[2],m3)
        if(m1==t1 and m2==t2 and m3==t3):
            return True
        else:
            return False