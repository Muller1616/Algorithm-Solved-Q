class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        new = []
        for i  in range(len(words)):
            if x in words[i]:
                new.append(i)
        return new