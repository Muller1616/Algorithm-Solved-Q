class Solution:
    def countDigits(self, num: int) -> int:
        num = str(num)
        count = 0
        for i in range(len(num)):
            if int(num) % int(num[i]) == 0:
                count += 1 
        return count 
            

        