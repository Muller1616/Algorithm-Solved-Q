from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        result = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            max_points = 0
            
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                # duplicate point
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1   # vertical line
                elif dy == 0:
                    dx = 1   # horizontal line
                
                slopes[(dx, dy)] += 1
                max_points = max(max_points, slopes[(dx, dy)])
            
            result = max(result, max_points + duplicates + 1)
        
        return result