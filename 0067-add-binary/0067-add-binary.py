class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        a,b = a[::-1], b[::-1]
        l_a = len(a)
        l_b = len(b)
        for i in range(max(l_a, l_b)):
            digit_A = ord(a[i]) - ord('0') if i < l_a else 0
            digit_B = ord(b[i]) - ord('0') if i < l_b else 0
            t = digit_A + digit_B + carry
            char = str(t % 2)
            res = char + res
            carry = t//2
        if carry:
            res = "1" + res
        return res
        