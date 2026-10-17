class Solution:
    def makesquare(self, matchsticks):
        if len(matchsticks) < 4 or sum(matchsticks) % 4:
            return False

        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return True

            for side in range(4):
                if sides[side] + matchsticks[i] <= target:
                    sides[side] += matchsticks[i]

                    if backtrack(i + 1):
                        return True

                    sides[side] -= matchsticks[i]

                if sides[side] == 0:
                    break

            return False

        return backtrack(0)