class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        new_arr = []
        for i in range(len(nums)):
            new_arr.append(nums[i])
        for i in range(0,len(new_arr),2):
            new_arr[i+1], new_arr[i] = new_arr[i], new_arr[i + 1]
        return new_arr

