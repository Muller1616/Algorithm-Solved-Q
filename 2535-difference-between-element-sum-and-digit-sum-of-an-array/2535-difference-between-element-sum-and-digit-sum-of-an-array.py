class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n = len(nums)
        new = []
        summ = 0
        for i in range(n):
            summ += nums[i]
        for num in nums:
            g = str(num)
            for s in g:
                new.append(int(s))
        ss = 0
        for i in range(len(new)):
            ss += new[i]
        return abs(summ - ss)