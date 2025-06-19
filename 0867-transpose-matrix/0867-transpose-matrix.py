class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        res = [[0]*row for _ in range(col)]
        for i in range(col):
            for j in range(row):
                res[i][j] = matrix[j][i]
        return res

        