class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirctsion = [(1,0), (0,1), (-1, 0), (0, -1)]
        visited = set()
        l_r = len(image)
        l_c = len(image[0])
        old_color = image[sr][sc]

        def dfs(row, col):
            if image[row][col] != old_color:
                return
            
            for r, c in dirctsion:
                n_r = row + r
                n_c = col + c
                if 0 <= n_r < l_r and 0 <= n_c < l_c and image[n_r][n_c] == old_color and (n_r, n_c) not in visited:
                    visited.add((n_r, n_c))
                    dfs(n_r, n_c)
                    image[n_r][n_c] = color
        
        dfs(sr,sc)
        image[sr][sc] = color
        return image
                    
                    
