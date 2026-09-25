class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1]
        indices = [0] * len(primes)

        for _ in range(1, n):
            next_num = min(
                ugly[indices[i]] * primes[i]
                for i in range(len(primes))
            )

            ugly.append(next_num)

            for i in range(len(primes)):
                if ugly[indices[i]] * primes[i] == next_num:
                    indices[i] += 1

        return ugly[-1]