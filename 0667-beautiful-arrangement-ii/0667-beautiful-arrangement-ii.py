class Solution:
    def constructArray(self, n, k):
        result = []
        left, right = 1, n

        while left <= right:
            if k > 1:
                if k % 2:
                    result.append(left)
                    left += 1
                else:
                    result.append(right)
                    right -= 1
                k -= 1
            else:
                result.extend(range(left, right + 1))
                break

        return result