class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dic={}
        def dp(i,j):
            if i>=m or j>=n:
                return 0
            if (i,j) not in dic:
                do=dp(i+1,j)
                ri=dp(i,j+1)
                da=dp(i+1,j+1)
                dic[(i,j)]=0
                if(matrix[i][j]=='1'):
                    dic[(i,j)]=1+min(do,ri,da)
            return dic[(i,j)]
        dp(0,0)
        return max(dic.values())**2