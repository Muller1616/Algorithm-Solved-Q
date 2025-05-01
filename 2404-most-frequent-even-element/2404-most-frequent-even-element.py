from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        li = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                li.append(nums[i])
        li = Counter(li)
        for key, value in li.items():
            if value ==max(li.values()):
                return key
        return -1
        