class Solution(object):
    def minSteps(self, n):
        steps = 0
        factor = 2
        
        # O(sqrt(N)) Time Execution: Trial Division Factorization
        while n > 1:
            # While cleanly divisible, extract the prime factor and add to operation count
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
            
        return steps