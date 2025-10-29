class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = 1
        while  right < len(nums):
            if nums[right] != 0 and nums[left] == 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
            if nums[left] != 0:
                left += 1
            right += 1
        return nums

        
