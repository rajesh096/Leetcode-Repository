class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for i in range(n)]
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        l=1

        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                matrix[top][i]=l
                l+=1
            top += 1

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                matrix[i][right]=l
                l+=1
            right -= 1

            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    matrix[bottom][i]=l
                    l+=1
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    matrix[i][left]=l
                    l+=1
                left += 1

        return matrix
