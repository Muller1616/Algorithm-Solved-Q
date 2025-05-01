class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        mul = 1
        summ = 0
        for i in range(len(s)):
            mul *= int(s[i])
        for j in range(len(s)):
            summ += int(s[j])
        return mul - summ


        