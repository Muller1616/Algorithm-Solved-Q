class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng = len(nums)
        for i in range(leng):
            for j in range(i+1, leng):
                if nums[i] + nums[j]==target:
                    return i,j
