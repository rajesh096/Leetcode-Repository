class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def bt(i,j):
            if(i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1 and obstacleGrid[i][j]!=1):
                return 1
            if(i>=len(obstacleGrid) or j>=len(obstacleGrid[0])):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if(obstacleGrid[i][j]==1):
                memo[(i,j)]=0
            else:
                memo[(i,j)]=bt(i+1,j)+bt(i,j+1)
            return memo[(i,j)]

        memo={}
        return bt(0,0)