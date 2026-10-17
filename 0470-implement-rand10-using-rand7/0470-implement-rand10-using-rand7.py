# rand7() is provided by LeetCode.

class Solution:
    def rand10(self):
        while True:
            row = rand7()
            col = rand7()
            num = (row - 1) * 7 + col

            if num <= 40:
                return 1 + (num - 1) % 10