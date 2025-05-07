class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = len(nums)//2
        d = Counter(nums)
        for key, value in d.items():
            if value > h:
                return key