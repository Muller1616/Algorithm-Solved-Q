class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        t_once = sum(nums)
        zeros, ones, maxsco = 0, 0, -1
        res = []

        for i in range(len(nums) + 1):
            sco = zeros + (t_once - ones)
            if sco > maxsco:
                res, maxsco = [i], sco
            elif sco == maxsco:
                res.append(i)
            if i < len(nums):
                zeros += nums[i] == 0
                ones += nums[i] == 1

        return res
