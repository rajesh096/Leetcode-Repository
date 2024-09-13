class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        p_xor=[0]*(len(arr)+1)
        for i in range(1,len(arr)+1):
            p_xor[i]=p_xor[i-1]^arr[i-1]
        res=[]
        for q in queries:
            l,r=q
            xor=p_xor[r+1]^p_xor[l]
            res.append(xor)
        return res