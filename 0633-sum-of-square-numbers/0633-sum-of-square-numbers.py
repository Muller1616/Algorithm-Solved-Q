import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))

        while a <= b:
            total = a * a + b * b

            if total == c:
                return True
            elif total < c:
                a += 1
            else:
                b -= 1

        return False
