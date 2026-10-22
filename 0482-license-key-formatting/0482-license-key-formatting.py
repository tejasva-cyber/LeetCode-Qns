class Solution:
    def licenseKeyFormatting(self, s, k):
        chars = s.replace("-", "").upper()
        first = len(chars) % k

        groups = []

        if first:
            groups.append(chars[:first])

        for i in range(first, len(chars), k):
            groups.append(chars[i:i + k])

        return "-".join(groups)