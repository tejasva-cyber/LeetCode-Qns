class Solution(object):
    def countPrimes(self, n):
        # Base case: There are no primes strictly less than 2.
        # And if n == 2, primes strictly less than 2 is 0.
        if n < 3:
            return 0
            
        # We exclusively track odd numbers to halve the memory footprint.
        # Index i represents the odd number: (2 * i) + 3
        # Index 0 = 3, Index 1 = 5, Index 2 = 7, etc.
        size = n // 2 - 1
        primes = [True] * size
        
        # We only need to sieve up to the square root of n
        root = int(n ** 0.5)
        limit = (root - 3) // 2 + 1
        
        for i in range(limit):
            if primes[i]:
                # Reconstruct the odd number from its index
                p = 2 * i + 3
                
                # Start marking at p^2. 
                # The index of p^2 in our odd-only array is exactly (p^2 - 3) // 2
                start = (p * p - 3) // 2
                
                # We step by p because jumping by p indices equals a value jump of 2p.
                # (We skip the even multiples entirely)
                length = (size - 1 - start) // p + 1
                primes[start::p] = [False] * length
                
        # Sum the True values (the odd primes) and add 1 for the only even prime (2)
        return sum(primes) + 1