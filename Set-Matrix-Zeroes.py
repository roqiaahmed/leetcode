class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = []
        y = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    x.append(r)
                    y.append(c)
        print("x",x)
        print("y",y)
        for i in range(len(matrix[0])):
            for r in x:
                matrix[r][i] = 0
        for i in range(len(matrix)):
            for c in y:
                matrix[i][c] = 0        
