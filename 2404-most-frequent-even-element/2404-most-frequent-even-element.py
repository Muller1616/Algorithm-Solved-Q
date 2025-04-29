from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        li = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                li.append(nums[i])
        if not li:
            return -1
        fre = Counter(li)
        m = max(fre.values())
        c = [num for num in fre if fre[num] == m]
        return min(c)


        