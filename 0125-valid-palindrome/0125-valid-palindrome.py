class Solution:
    def isPalindrome(self, s):
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        return filtered == filtered[::-1]