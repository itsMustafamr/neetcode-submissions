class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # #way - 1
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] == target:
        #             return True
        # return False

        # i did - wrongggggg
        # for i in range(len(matrix)):
        #     for j in range(i + 1, len(matrix)):
        #         if matrix[i][j] == target:
        #             return True    
        # return False

        # way - 2
        # log m + log n -> we do 2 binary searches (first to get which row then 2nd to find val)
        rows, cols = len(matrix), len(matrix[0])

        toprow, botrow = 0, rows - 1
        while toprow <= botrow :
            row = (toprow + botrow) // 2
            if target > matrix[row][-1]:
                toprow = row + 1
            elif target < matrix[row][0]:
                botrow = row - 1
            else:
                break
        
        if not (toprow <= botrow):
            return False
        row = (toprow + botrow) // 2
        l,r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

