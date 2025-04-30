class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)