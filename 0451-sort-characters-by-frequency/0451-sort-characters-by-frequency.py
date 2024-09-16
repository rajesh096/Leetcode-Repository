class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d=dict(sorted(d.items(), key=lambda item:item[1],reverse=True))
        st=""
        for i,j in d.items():
            st+=i*j
        return st