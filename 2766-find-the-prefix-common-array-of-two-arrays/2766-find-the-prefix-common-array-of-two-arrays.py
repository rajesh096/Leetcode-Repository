class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dic = {k:v for k,v in (zip([i for i in range(len(A))],[[] for _ in range(len(A))]))}
        for i in range(len(A)):
            dic[i].append(A[i])
            dic[i].append(B[i])
        print(dic)
        res=[]
        for i,j in dic.items():
            a=[]
            count=0
            for k in range(i+1):
                r=dic[k]
                a.append(r[0])
            for k in range(i+1):
                r=dic[k]
                if r[1] in a:
                    count+=1
            res.append(count)
        return res