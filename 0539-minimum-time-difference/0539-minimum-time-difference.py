class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        k=[]
        for i in timePoints:
            l=i.split(":")
            k.append(int(l[0])*60+int(l[1]))
        k=sorted(k)
        m=float('inf')
        for i in range(1,len(k)):
            if k[i]-k[i-1]<m:
                m=k[i]-k[i-1]
        print(m)
        m=min(m,1440-k[-1]+k[0])
        print(m)
        return m