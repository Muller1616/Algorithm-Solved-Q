class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        re = []
        for num in nums1:
            next_gre = -1
            found = False
            for i in range(len(nums2)):
                if nums2[i] == num:
                    found = True
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > num:
                            next_gre = nums2[j]
                            break
                    break
            re.append(next_gre)
        return re