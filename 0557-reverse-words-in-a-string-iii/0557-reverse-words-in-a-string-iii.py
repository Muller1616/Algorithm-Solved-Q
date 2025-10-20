class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split(' ')
        rw = []

        for word in w:
            rev = word[::-1]
            rw.append(rev)

        re = " ".join(rw)
        return re

        