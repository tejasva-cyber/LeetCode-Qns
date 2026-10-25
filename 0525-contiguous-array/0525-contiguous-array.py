class Solution:
    def findMaxLength(self, nums):
        first = {0: -1}
        balance = 0
        answer = 0

        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1

            if balance in first:
                answer = max(answer, i - first[balance])
            else:
                first[balance] = i

        return answer