class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = sorted(nums)
        s = s[::-1]
        return s[k-1]
        