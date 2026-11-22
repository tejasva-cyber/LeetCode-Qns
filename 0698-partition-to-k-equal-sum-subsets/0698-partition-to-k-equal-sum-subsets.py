class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)

        if total % k:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(index):
            if index == len(nums):
                return True

            value = nums[index]
            seen = set()

            for i in range(k):
                if buckets[i] + value > target or buckets[i] in seen:
                    continue

                seen.add(buckets[i])
                buckets[i] += value

                if backtrack(index + 1):
                    return True

                buckets[i] -= value

                if buckets[i] == 0:
                    break

            return False

        return backtrack(0)