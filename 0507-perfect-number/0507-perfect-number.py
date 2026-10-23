class Solution(object):
    def checkPerfectNumber(self, num):
        # Base state: 1 cannot be a perfect number because it has no positive divisors excluding itself.
        if num <= 1:
            return False
            
        # 1 is universally a proper divisor
        divisor_sum = 1 
        
        # O(sqrt(N)) Execution: Bounding the loop to the square root of the target
        i = 2
        while i * i <= num:
            if num % i == 0:
                divisor_sum += i
                # Ensure we don't double-count the perfect square root
                if i * i != num:
                    divisor_sum += num // i
            i += 1
            
        return divisor_sum == num