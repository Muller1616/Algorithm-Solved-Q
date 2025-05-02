class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n =Counter(nums)
        if len(n) == 1:
            return "equilateral"
        elif len(n) == 2:
            return "isosceles"
        elif len(n) ==3:
            if nums[0] + nums[1]>nums[2] and nums[0] + nums[2]>nums[1] and nums[1] + nums[2]>nums[0]:
                return "scalene"
            else:
                return "none"
                
        