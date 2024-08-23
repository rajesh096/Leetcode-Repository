class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            s=0
            e=m-1
            pos=-1
            while(s<=e):
                mid=(s+e)//2
                if(grid[i][mid]<0):
                    e=mid-1
                    pos=mid
                else:
                    s=mid+1
            if pos!=-1:
                count+=(m-pos)
        return count