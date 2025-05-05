class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        re = [[1]]
        for i in range(numRows - 1):
            t = [0] + re[-1] + [0]
            row  = []
            for j in range(len(re[-1]) + 1):
                row.append(t[j] + t[j+1])
            re.append(row)
        return re
        