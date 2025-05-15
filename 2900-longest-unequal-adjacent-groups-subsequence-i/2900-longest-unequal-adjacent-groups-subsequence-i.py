class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        last = groups[0]
        ans = [words[0]]
        for i in range(1,n):
            if groups[i] != last:
                last = groups[i]
                ans.append(words[i])
        return ans