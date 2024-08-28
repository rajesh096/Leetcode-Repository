from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid: List[List[int]], x: int, y: int, island_cells: List[tuple]):
            # Stack-based DFS to explore all cells of the current island
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]) and grid[cx][cy] == 1:
                    grid[cx][cy] = 0  # Mark cell as visited
                    island_cells.append((cx, cy))
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        stack.append((cx + dx, cy + dy))
        
        def is_sub_island(island_cells: List[tuple]) -> bool:
            # Check if all cells of the island in grid2 are land in grid1
            for x, y in island_cells:
                if grid1[x][y] == 0:
                    return False
            return True

        m, n = len(grid2), len(grid2[0])
        sub_island_count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    island_cells = []
                    dfs(grid2, i, j, island_cells)
                    if is_sub_island(island_cells):
                        sub_island_count += 1
        
        return sub_island_count