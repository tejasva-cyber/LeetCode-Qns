class Solution:
    def arrayNesting(self, nums):
        n = len(nums)
        visited = [False] * n
        answer = 0

        for i in range(n):
            count = 0
            j = i

            while not visited[j]:
                visited[j] = True
                count += 1
                j = nums[j]

            answer = max(answer, count)

        return answer