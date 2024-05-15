class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        direcsion = [(1, 0), (-1, 0), (0, -1), (0 , 1)]
        visited = set()
        n_islands = 0
        n_row = len(grid) - 1 
        n_col = len(grid[0])- 1

        def bfs(r, c):
            if grid[r][c] == "0":
                return
            # print("========>. ",(r,c))
            # print(visited)
            for nr, nc in direcsion:
                c_row = r + nr
                c_col = c + nc
                if  0 <= c_row <= n_row and 0 <= c_col <= n_col and grid[c_row][c_col] == "1" and (c_row, c_col) not in visited:
                    visited.add((c_row, c_col))
                    bfs(c_row, c_col)


        for r in range(n_row + 1):
            for c in range(n_col + 1):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    n_islands += 1
                    bfs(r, c)
                    # print("++++++++++++++++++++++++++++++++++")
                    
        
        return n_islands
