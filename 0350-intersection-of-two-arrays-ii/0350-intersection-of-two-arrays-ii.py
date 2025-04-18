from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        outp = []
        for i in nums2:
            if c[i] > 0:
                outp.append(i)
                c[i] -= 1
        return outp        