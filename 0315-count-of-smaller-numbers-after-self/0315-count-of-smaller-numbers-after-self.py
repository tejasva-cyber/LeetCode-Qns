class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        result = [0] * n
        values = sorted(set(nums))
        rank = {value: i + 1 for i, value in enumerate(values)}

        bit = [0] * (len(values) + 1)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        for i in range(n - 1, -1, -1):
            r = rank[nums[i]]
            result[i] = query(r - 1)
            update(r)

        return result