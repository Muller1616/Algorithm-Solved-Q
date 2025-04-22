class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sett = list(set(nums))
        lenset = len(sett)
        sett.sort(reverse = True)
        if lenset >= 3:
            return sett[2]
        else:
            return sett[0] 