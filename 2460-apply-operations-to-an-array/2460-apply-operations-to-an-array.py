class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                continue
            else:
                nums[i-1] *= 2
                nums[i] = 0
        pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos,n):
            nums[i] = 0
        return nums
        