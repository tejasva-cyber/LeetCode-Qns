class Solution:
    def largestPalindrome(self, n):
        if n == 1:
            return 9

        upper = 10**n - 1
        lower = 10**(n - 1)

        for left in range(upper, lower - 1, -1):
            palindrome = int(str(left) + str(left)[::-1])

            for x in range(upper, lower - 1, -1):
                if x * x < palindrome:
                    break

                if palindrome % x == 0 and lower <= palindrome // x <= upper:
                    return palindrome % 1337

        return 0