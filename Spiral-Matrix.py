class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1

        while l <= r and t <= b:
            # from top-left to top-right
            if t <= b:
                for col in range(l, r + 1):
                    spiral.append(matrix[t][col])
                t += 1

            # from right-top to right-bottom
            if r >= l:
                for row in range(t, b + 1):
                    spiral.append(matrix[row][r])
                r -= 1

            # from bottom-right to bottom-left
            if b >= t:
                for col in range(r,l - 1,-1):
                    spiral.append(matrix[b][col])
                b -= 1

            # from left-bottom to left-top
            if l <= r:
                for row in range(b, t - 1, -1):
                    spiral.append(matrix[row][l])
                l += 1

        return spiral
