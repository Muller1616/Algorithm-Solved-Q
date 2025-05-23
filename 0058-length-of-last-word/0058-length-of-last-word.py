class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n-1,-1, -1):
            if s[i].isalpha():
                count += 1
            elif count>0:
                break
        return count