class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n=[]
        for i in range(len(accounts)):
            summ=0
            for j in range(len(accounts[i])):
                summ += accounts[i][j]
            n.append(summ)
        return max(n)

        