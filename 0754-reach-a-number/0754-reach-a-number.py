class Solution:
    def reachNumber(self, target):
        target = abs(target)
        total = 0
        steps = 0

        while total < target or (total - target) % 2:
            steps += 1
            total += steps

        return steps