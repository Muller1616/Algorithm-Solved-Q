from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        count = Counter(s)
        for i in range(n):
            if count[s[i]] == 1:
                return i
        return -1


        