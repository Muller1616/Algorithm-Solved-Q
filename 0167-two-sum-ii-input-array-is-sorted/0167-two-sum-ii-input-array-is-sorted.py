class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers) - 1
        while l < r:
            ss = numbers[l] + numbers[r]
            if ss == target:
                return [l + 1, r + 1]
            elif ss < target:
                l += 1
            else:
                r -= 1
        return []