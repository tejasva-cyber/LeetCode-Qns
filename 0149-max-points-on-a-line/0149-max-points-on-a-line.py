class Solution(object):
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
            
        # 1. Dependency-Free GCD Implementation
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        result = 0
        
        for i in range(len(points)):
            slopes = {}
            local_max = 0
            
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                g = get_gcd(dx, dy)
                dx //= g
                dy //= g
                
                # 2. Force strict directional vector normalization
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                    
                slope = (dy, dx)
                slopes[slope] = slopes.get(slope, 0) + 1
                
                # 3. Track running max to avoid incompatible max() syntax
                local_max = max(local_max, slopes[slope])
                
            result = max(result, local_max + 1)
            
        return result