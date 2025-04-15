class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        ls = []

        for digit in digits:
            a += str(digit)
        b = int(a)
        c = str(b+1)
        for d in c:    
            ls.append(int(d))
        return ls