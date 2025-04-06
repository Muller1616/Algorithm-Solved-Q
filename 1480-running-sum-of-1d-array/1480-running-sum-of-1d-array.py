class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        for i in range(1,length_nums):
            nums[i] += nums[i-1]
        return nums
