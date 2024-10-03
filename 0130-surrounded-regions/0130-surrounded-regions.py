class Solution:
    def re(self,i,j,grid):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='O':
            return 0
        grid[i][j]='T'

        self.re(i-1,j,grid)
        self.re(i+1,j,grid)
        self.re(i,j-1,grid)
        self.re(i,j+1,grid)
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i<=0 or j<=0 or i==len(grid)-1 or j==len(grid[0])-1:
                    if(grid[i][j]=='O'):
                        self.re(i,j,grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='O':
                    grid[i][j]='X'
                elif grid[i][j]=='T':
                    grid[i][j]='O'