class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right +1):
            if not any(start <= num <= end  for start, end in ranges):
                return False
        return True
                
        