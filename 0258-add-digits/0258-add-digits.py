class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s) != 1:
            summ = 0
            for i in range(len(s)):
                summ += int(s[i])
            s = str(summ)
        return int(s)
                