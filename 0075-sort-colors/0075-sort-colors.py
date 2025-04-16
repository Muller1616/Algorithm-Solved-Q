class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lower = 0
        middle = 0
        end = len(nums) -1
        def swap(middle,b):
            first = nums[middle]
            nums[middle] = nums[b] 
            nums[b] = first
        while middle <= end:
            if nums[middle] == 0:
                swap(lower,middle)
                lower += 1
            elif nums[middle] == 2:
                swap(middle, end)
                end -= 1
                middle -= 1
            middle += 1

