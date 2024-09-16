class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        d=dict(sorted(d.items(), key=lambda item:item[1],reverse=True))
        st=""
        for i,j in d.items():
            st+=i*j
        return st