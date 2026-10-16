class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1 == 0:
            return 0

        s1_count = 0
        s2_count = 0
        index = 0
        seen = {}

        while s1_count < n1:
            s1_count += 1

            for ch in s1:
                if ch == s2[index]:
                    index += 1

                    if index == len(s2):
                        s2_count += 1
                        index = 0

            if index in seen:
                prev_s1, prev_s2 = seen[index]
                cycle_s1 = s1_count - prev_s1
                cycle_s2 = s2_count - prev_s2

                remaining = n1 - s1_count
                cycles = remaining // cycle_s1

                s1_count += cycles * cycle_s1
                s2_count += cycles * cycle_s2
            else:
                seen[index] = (s1_count, s2_count)

        return s2_count // n2