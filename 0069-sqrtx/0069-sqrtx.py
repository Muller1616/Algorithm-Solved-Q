class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left , right = 0, x
        result = 0
        while left <= right:
            mid = left + ((right - left)) //2
            if mid**2 > x:
                right = mid -1 
            elif mid**2 < x:
                left = mid +1
                result = mid
            else:
                return mid
        return result
        