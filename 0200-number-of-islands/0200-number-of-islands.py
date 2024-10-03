class Solution:
    def re(self,i,j,grid):
        if i<0 or j<0 or i==len(grid) or j==len(grid[0]) or grid[i][j]=='0':
            return 0
        grid[i][j]='0'

        self.re(i-1,j,grid)
        self.re(i+1,j,grid)
        self.re(i,j-1,grid)
        self.re(i,j+1,grid)
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    count+=1
                    self.re(i,j,grid)
        return count

        