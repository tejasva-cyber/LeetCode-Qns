class Solution:
    def lexicalOrder(self, n):
        result = []

        def dfs(num):
            if num > n:
                return

            result.append(num)

            for digit in range(10):
                nxt = num * 10 + digit
                if nxt > n:
                    break
                dfs(nxt)

        for i in range(1, 10):
            dfs(i)

        return result