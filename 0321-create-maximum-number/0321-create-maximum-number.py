class Solution:
    def maxNumber(self, nums1, nums2, k):

        def pick(nums, k):
            stack = []
            remove = len(nums) - k

            for num in nums:
                while stack and remove and stack[-1] < num:
                    stack.pop()
                    remove -= 1

                stack.append(num)

            return stack[:k]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        def greater(a, i, b, j):
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1

            return j == len(b) or (i < len(a) and a[i] > b[j])

        def merge_fast(a, b):
            result = []
            i = j = 0

            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1

            return result

        best = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            a = pick(nums1, i)
            b = pick(nums2, k - i)
            candidate = merge_fast(a, b)

            if candidate > best:
                best = candidate

        return best