class Solution:
    def arraySign(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            summ = prod(nums)
            if summ > 0:
                return 1
            elif summ < 0:
                return -1
            else:
                return 0