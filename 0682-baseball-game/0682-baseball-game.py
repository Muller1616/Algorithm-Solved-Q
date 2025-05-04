class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for t in operations:
            if t == "C":
                record.pop()
            elif t == "D":
                record.append(2 * record[-1])
            elif t == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(t))
        return sum(record)
