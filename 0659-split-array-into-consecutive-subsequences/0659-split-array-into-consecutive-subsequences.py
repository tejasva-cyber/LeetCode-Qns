from collections import Counter

class Solution:
    def isPossible(self, nums):
        count = Counter(nums)
        need = Counter()

        for num in nums:
            if count[num] == 0:
                continue

            count[num] -= 1

            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1

            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                need[num + 3] += 1

            else:
                return False

        return True