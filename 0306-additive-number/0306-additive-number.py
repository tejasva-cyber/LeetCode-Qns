class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        def dfs(index, a, b, count):
            if index == n:
                return count >= 3

            for end in range(index + 1, n + 1):
                if end > index + 1 and num[index] == '0':
                    break

                c = int(num[index:end])

                if count >= 2 and c != a + b:
                    continue

                if dfs(end, b, c, count + 1):
                    return True

            return False

        for i in range(1, n):
            if i > 1 and num[0] == '0':
                break

            a = int(num[:i])

            for j in range(i + 1, n):
                if j > i + 1 and num[i] == '0':
                    break

                b = int(num[i:j])

                if dfs(j, a, b, 2):
                    return True

        return False