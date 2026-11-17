class Solution:
    def judgePoint24(self, cards):
        EPS = 1e-6

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    remaining = [
                        nums[k] for k in range(len(nums))
                        if k != i and k != j
                    ]

                    a, b = nums[i], nums[j]

                    candidates = [a + b, a - b, a * b]

                    if abs(b) > EPS:
                        candidates.append(a / b)

                    for value in candidates:
                        if solve(remaining + [value]):
                            return True

            return False

        return solve([float(x) for x in cards])