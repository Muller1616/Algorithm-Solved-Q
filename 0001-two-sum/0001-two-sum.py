class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,value in enumerate(nums):
            s = target - value
            if s in dic:
                return [dic[s], i]
            dic[value] = i