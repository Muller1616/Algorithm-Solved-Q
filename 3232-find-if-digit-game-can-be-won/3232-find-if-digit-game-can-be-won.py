class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        d = 0
        ss = 0
        for i in range(len(nums)):
            if nums[i] >=10:
                d +=nums[i]
            else:
                ss += nums[i]
        return d!=ss