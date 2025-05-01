class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num = []
        for i in range(len(nums)):
            s = pow(nums[i], 2)
            num.append(s)
        num.sort()
        return num