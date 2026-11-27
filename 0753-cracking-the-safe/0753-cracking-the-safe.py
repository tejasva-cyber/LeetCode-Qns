class Solution(object):
    def crackSafe(self, n, k):
        digits = [str(d) for d in range(k)]
        res = []
        w = [0]

        while w:
            m = len(w)
            # Emit every Lyndon word whose length divides n
            if n % m == 0:
                for idx in w:
                    res.append(digits[idx])

            # Periodically repeat w up to length n
            for i in range(n - m):
                w.append(w[i])

            # Strip trailing max digits and advance to the next lexicographical word
            while w and w[-1] == k - 1:
                w.pop()
            if w:
                w[-1] += 1

        # Unwrap the cyclic De Bruijn sequence into a linear string
        if n > 1:
            res.append('0' * (n - 1))

        return ''.join(res)