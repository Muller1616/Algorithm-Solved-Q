class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        d = set(nums)
        l = len(d)
        if l<n:
            return True
        return False